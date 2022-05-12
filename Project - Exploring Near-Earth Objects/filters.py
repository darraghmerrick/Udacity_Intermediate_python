"""Provide filters for querying close approaches and limiting results.
The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.
This function can be thought to return a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest
from the supplied `CloseApproach`.
The `limit` function simply limits the maximum number of values produced by an
iterator.
You'll edit this file in Tasks 3a and 3c.
"""
import operator


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    """A general superclass for filters on comparable attributes.
    An `AttributeFilter` represents the search criteria pattern comparing some
    attribute of a close approach (or its attached NEO) to a reference value.
    It essentially functions as a callable predicate for whether a
    `CloseApproach` object satisfies the encoded criterion.
    It is constructed with a comparator operator and a reference value, and
    calling the filter (with __call__) executes `get(approach) OP value` (in
    infix notation).
    Concrete subclasses can override the `get` classmethod to provide custom
    behavior to fetch a desired attribute from the given `CloseApproach`.
    """

    def __init__(self, op, value):
        """Construct a new `AttributeFilter` from a binary predicate and value.
        The reference value will be supplied as the second (right-hand side)
        argument to the operator function. For example, an `AttributeFilter`
        with `op=operator.le` and `value=10` will, when called on an approach,
        evaluate `some_attribute <= 10`.
        :param op: A 2-argument predicate comparator (such as `operator.le`).
        :param value: The reference value to compare against.
        """
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach.
        Concrete subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`.
        :param approach: A `CloseApproach` on which to evaluate this filter.
        :return: The value of an attribute of interest, comparable to
            `self.value` via `self.op`.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        """Return `repr(self)` string representation of object."""
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, \
            value={self.value})"


def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    """Create a collection of filters from user-specified criteria.
    Each of these arguments is provided by the main module with a value from
    the user's options at the command line. Each one corresponds to a different
    type of filter. For example, the `--date` option corresponds to the `date`
    argument, and represents a filter that selects close approaches that
    occurred on exactly that given date. Similarly, the `--min-distance` option
    corresponds to the `distance_min` argument, and represents a filter that
    selects close approaches whose nominal approach distance is at least that
    far away from Earth. Each option is `None` if not specified at the command
    line (in particular, this means that the `--not-hazardous` flag results in
    `hazardous=False`, not to be confused with `hazardous=None`).
    The return value must be compatible with the `query` method of
    `NEODatabase` because the main module directly passes this result to that
    method. For now, this can be thought of as a collection of
    `AttributeFilter`s.
    :param date: A `date` on which a matching `CloseApproach` occurs.
    :param start_date: A `date` on or after which a matching `CloseApproach`
        occurs.
    :param end_date: A `date` on or before which a matching `CloseApproach`
        occurs.
    :param distance_min: A minimum nominal approach distance for a matching
        `CloseApproach`.
    :param distance_max: A maximum nominal approach distance for a matching
        `CloseApproach`.
    :param velocity_min: A minimum relative approach velocity for a matching
        `CloseApproach`.
    :param velocity_max: A maximum relative approach velocity for a matching
        `CloseApproach`.
    :param diameter_min: A minimum diameter of the NEO of a matching
        `CloseApproach`.
    :param diameter_max: A maximum diameter of the NEO of a matching
        `CloseApproach`.
    :param hazardous: Whether the NEO of a matching `CloseApproach` is
        potentially hazardous.
    :return: A collection of filters for use with `query`.
    """
    filters = []

    if date is not None:
        filters.append(
            CreateFilter(operator.eq, date, 'approach.time', fn='date')
        )

    if start_date is not None:
        filters.append(
            CreateFilter(operator.ge, start_date, 'approach.time', fn='date')
        )

    if end_date is not None:
        filters.append(
            CreateFilter(operator.le, end_date, 'approach.time', fn='date')
        )

    if distance_min is not None:
        filters.append(
            CreateFilter(operator.ge, distance_min, 'approach.distance')
        )

    if distance_max is not None:
        filters.append(
            CreateFilter(operator.le, distance_max, 'approach.distance')
        )

    if velocity_min is not None:
        filters.append(
            CreateFilter(operator.ge, velocity_min, 'approach.velocity')
        )

    if velocity_max is not None:
        filters.append(
            CreateFilter(operator.le, velocity_max, 'approach.velocity')
        )

    if diameter_min is not None:
        filters.append(
            CreateFilter(operator.ge, diameter_min, 'approach.neo.diameter')
        )

    if diameter_max is not None:
        filters.append(
            CreateFilter(operator.le, diameter_max, 'approach.neo.diameter')
        )

    if hazardous is not None:
        filters.append(
            CreateFilter(operator.eq, hazardous, 'approach.neo.hazardous')
        )

    return filters


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.
    If `n` is 0 or None, don't limit the iterator at all.
    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    if n is None or n == 0:
        for i, element in enumerate(iterator):
            try:
                yield element
            except StopIteration:
                pass
    else:
        it = iter(range(n))
        for i, element in enumerate(iterator):
            try:
                nexti = next(it)
                yield element
            except StopIteration:
                pass


def CreateFilter(op, value, param, fn=None):
    """Create a filter class object based on the passed in parameters."""

    class GeneralFilter(AttributeFilter):
        def __init__(self):
            self.op = op
            self.value = value

        def __call__(self, approach):
            return self.op(self.get(approach), self.value)

        @classmethod
        def get(cls, approach):
            params = param.split('.')

            v = locals()[params[0]]

            for elem in params[1:]:
                v = getattr(v, elem)

            if fn:
                return getattr(v, fn)()
            else:
                return v

    return GeneralFilter()