"""
Use of with Statements to Open and Close Files
    Instead of using try-except-finally blocks to handle file opening and
    closing operations, a much cleaner way of doing this in Python
    is using the with statement. You can use a with statement in
    Python such that you do not have to close the file handler object

    with open(file, mode) as file_handler:
        Statement_1
        Statement_2
        ...
        Statement_N

    with and as are keywords.
    with is followed by open() function and ends with a colon
    as keyword acts like an alias and is used to assign the
    returning object from the open() function to a new variable
    file_handler.

    The with statement creates a context manager and it will
    automatically close the file handler object for you when
    you are done with it, even if an exception is raised on
    the way, and thus properly managing resources

    The protocol, such as a class consisting of the __enter__()
    and __exit__() methods, is known as the "context management
    protocol", and the object that implements that protocol is
    known as the "context manager". The evaluation of the with
    statement results in an object called a "context manager"
    that supports the "context management protocol". The __enter__()
    method is executed when the control enters the code block inside
    the with statement block context. It returns an object that can
    be used within the context. When control leaves with with block
    context, then the __exit__() method is called to clean up any
    resources being used. Thus, the resources are allocated and
    deallocated when the program requires it.

    You can also use a with statement to open more than one file
        with open(in_filename) as in_file, open(out_filename, "w") as out_file:
            out_file.write(parsed_line)
"""

