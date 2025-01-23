class Square:
    """
    A class that describes a typical square
    
    === Public Attribute ===
    
    side: a side of a square
    area: an area of a square
    """
    side: float
    area: float
    
    # classes have methods which are functions that only work on themselves
    def __init__(self, side: float) -> None:
        self.side = side
        self.area = side ** 2
        
    def get_area(self) -> float:
        return self.area
    
class Cube:
    """
    A cube 3D object
    
    === Public Attribute ===
    side: a side of a cube
    
    >>> x = cube(2)
    >>> x.get_volume()
    8
    >>> x.get_surface_area()
    24
    >>> x.get_side()
    2
    """
    def __init__(self, side):
        self.side = side
        
    def get_side(self):
        return self.side
    
    def get_surface_area(self):
        return round(6 * (self.side ** 2), 2)
    
    def get_volume(self):
        return round(self.side ** 3, 2)
    
    
class Table:
    """
    Information about a table.

    """
    def __init__(self, table_id: int, num_seats: int, num_occupied: int) -> None:
        """ 
        Initialize a new table with table ID table_id, num_seats seats, and 
        num_occupied seats occupied.
        
        >>> table1 = Table(1, 4, 0)
        >>> table1.id
        1
        >>> table1.num_seats
        4
        >>> table1.num_occupied
        0
        """
        self.id = table_id
        self.num_seats = num_seats
        self.num_occupied = num_occupied

    def __str__(self) -> str:
        """
        Return a string representation of this table.
    
        >>> table4 = Table(4, 6, 3)
        >>> str(table4)
        'Table 4: 3 of 6 seats occupied
        """
        # return "Table " + str(self.id) + ": "+ str(self.num_occupied) + " of " + str(self.num_seats) + " seats occupied"  
        # return f"Table {self.id}: {self.num_occupied} of {self.num_seats} seats occupied"
        return "Table {}： {} of {} seats occupied".format(self.id, self.num_occupied, self.num_seats)

    def set_occupancy(self, num_occupied: int) -> None:
        """
        Set the number of seats occupied at this table to num_occupied.
        
        Precondition: self.num_seats >= num_occupied
        
        >>> table1 = Table(1, 4, 0)
        >>> table1.num_occupied
        0
        
        >>> table1.set_occupancy(3)
        >>> table1.num_occupied
        3
        """
        
        return self.num.ocuppied
    
class Room:
    """A hotel room. """
    def __init__(self, num: int, max_occupancy: int) -> None:
        """Initialize a room with the room number num and a maximunm occupancy of 
        max_occupancy that is not currently booked.
        
        >>> r = Room(404, 2)
        >>> r.room_number
        404
        >>> r.max_occupancy
        2
        >>> r.is_booked
        False
        """
        self.room_number = num
        self.max_occupancy = max_occupancy
        self.is_booked = False
        
        
    def book_room(self) -> bool:
        """If this room is not currently booked, update this room's booking
        status to booked and return True. Otherwise, return False adn do not 
        change the booking status.
        
        >>> r = Room(401, 4)
        >>> r.book_room()
        True
        >>> r.is_booked
        True
        >>> r,book_room()
        False
        >>> r.is_booked
        True
        """
        #if self.is_booked is True:
        #if self.is_booked == True:
        if self.is_booked:
            return False
        else:
            self.is_booked = True
            return True      
       
        