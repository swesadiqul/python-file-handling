# Other File Operation
# There are various other methods that are used with file objects for different operations:


"""
#Method	            #Function Description
flush()	            Flush the internal buffer. It has no return value
detach()	        Returns the separated raw stream from the buffer
readable()	        Returns true if the file stream can be read
seek(offset, from)	Used to set the file object’s current position to offset ​bytes ​from ​the bytes given
tell()	            Returns the file current position
seekable()	        Returns true if the file stream allows random access
writable()	        Returns true if the file allows being written into
fileno()	        Returns the file number (file descriptor) used by Operating System for I/O operations
next()	            Returns the next line of the file
truncate([size])	Truncates the file to the size (optional) specified.

"""