"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation, name=None, diameter=float('nan'), hazardous="", approaches=[], **info):
        """Create a new `NearEarthObject`.
        :param designation: (str) Unique identifier of the Near Earth Object.
        :param name: (str) Name of the NEO.
        :param diameter: (float) diameter in km.3ca = CloseApproach(
        :param hazardous: (bool) If NASA classified the NEO as hazardous.
        :param approaches: (list) approaches to earth of the NEO
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        
        # Assign information from the arguments passed to the constructor:
        #Assign designation
        self.designation = str(designation)
        #Assign name
        if name.strip() == "":
            self.name = None
        else:
            self.name = str(name)
        # Assign diameter
        try:
            self.diameter = float(diameter)
        except ValueError:
            self.diameter = float("nan")
        # Assign hazardous
        if hazardous.lower() == "y":
            self.hazardous = True
        else:
            self.hazardous = False
        # Assign approaches
        self.approaches = list(approaches)

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is None:
            return f"{self.designation}"
        else:
            return f"{self.designation} ({self.name})"

    def __str__(self):
      """Return `str(self)`."""
      if not self.hazardous:
            hazard = " not"
      else:
            hazard = ""

      if math.isnan(self.diameter):
            diameter_string = "diameter is not known"
      else:
            diameter_string = f"has a diameter of {self.diameter:.3f} km"
      return f"{self.fullname} {diameter_string} and is{hazard} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time, distance, velocity, **info):
        """Create a new `CloseApproach`.

        :param designation: (str) unique id of NEO
        :param time: (UTC date and time) closest approach to earth in format %Y-%b-%d %H:%M
        :param distance: (float) closest distance to earth
        :param velocity: (float) in km/s when passing earth
        :param neo: A NEO object
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = str(designation)

        self.time = cd_to_datetime(time)

        try:
            self.distance = float(distance)
        except ValueError:
            self.distance = float("nan")
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None


    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        return f"A CloseApproach in {self.time_str!r} with distance {self.distance:.2f}, velocity {self.velocity:.2f} and NEO {self.neo!r}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
