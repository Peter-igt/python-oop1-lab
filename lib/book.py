#!/usr/bin/env python3

class Book:
    """
    Represents a book with a title and page count.
    Allows users to read through pages.
    """
    
    def __init__(self, title, page_count):
        """
        Initialize a Book object.
        
        Args:
            title (str): The title of the book
            page_count (int): The total number of pages in the book
        """
        self.title = title
        self._page_count = None
        # Use the property setter to validate page_count
        self.page_count = page_count
    
    @property
    def page_count(self):
        """
        Get the page count of the book.
        
        Returns:
            int: The total number of pages
        """
        return self._page_count
    
    @page_count.setter
    def page_count(self, value):
        """
        Set the page count with validation.
        Ensures the value is an integer, prints error message if not.
        
        Args:
            value: The value to set as page_count
        """
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")
    
    def turn_page(self):
        """
        Simulate turning a page in the book.
        Prints a message indicating the page has been turned.
        """
        print("Flipping the page...wow, you read fast!")
        