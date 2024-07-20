def auto_repr(args, kwargs):


    def wrapper(cls):
        # old_repr = cls.__repr__

        def new_repr(self):
            listing_args = [str(self.__dict__[i]) if not isinstance(self.__dict__[i], str) else str("'" + self.__dict__[i] + "'") for
                            i in self.__dict__ if i in args]
            listing_kwargs = [str(str(i) + '=' + "'" + self.__dict__[i] + "'") for i in self.__dict__ if i in kwargs]

            final_list = listing_args + listing_kwargs

            return f'{self.__class__.__name__}({', '.join(final_list)})'

        cls.__repr__ = new_repr

        return cls

    return wrapper
