"""
csv Module

csv.reader(csvfile)         returns a csv reader object which will iterate
                            over lines in the given csvfile. If csv is a
                            file object, it should be opened with
                            newline=" "

csv.writer(csvfile)         returns a csv writer object responsible for
                            converting the user's data into comma
                            separated strings on the give file-like object

csvwriter.writerow()        where csvwriter is the object returned by the
                            writer method and writerow() method will write
                            the row argument to the writer() method's file
                            object.
                            A row must be an iterable of strings or numbers
                            for writer objects, and a dictionary mapping
                            fieldnames to strings or numbers (by passing
                            them through str() first) for DictWriter objects

csvwriter.writerows()       write all the rows argument (a list of row
                            objects) to the writer() method's file object

class csv.DictReader(       creates an object that operates like a regular
    f, fieldnames=None,     reader but maps the information in each row to
    restkey=None)           a regular dictionary whose keys are given by
                            the optional fieldnames argument.
                            If fieldnames omitted then the first row of
                            file f will be used as fieldnames. If a row
                            has more fields that the fieldnames, then the
                            remaining data is put in a list and stored with
                            the fieldname specified by restkey keyword
                            argument (which by default is none). If a
                            non-blank row has fewer fields than fieldnames
                            the missing values are filled-in with None

class csv.DictWriter(       creates an object that operates like a regular
    f, fieldnames,          reader but maps dictionaries onto output rows
    extrasaction="raise")   Fieldnames is a sequence of keys that identify
                            the order in which the values in the dictionary
                            are passed to the writerow() method and are
                            written to file f. If the dictionary passed
                            to writerow() method contains a key not found in
                            fieldnames, then the optional extrasaction
                            argument indicates what action to take. If set
                            to "raise", a ValueError is raised. If set
                            to "ignore", extra values in the dictionary
                            are ignored.

"""