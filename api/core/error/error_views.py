from .error import ErrorHelper


class TypeModelError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого типа не существует", status=self.NOT_FOUND)


class EventModelError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого события не существует", status=self.NOT_FOUND)


class PersonModelError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такой персоны не существует", status=self.NOT_FOUND)

