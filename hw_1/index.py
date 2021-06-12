from pickle import dumps as bin_dumps
from json import dumps


# meta


class Meta(type):
    counter = 0

    def __new__(cls,   *args):
        cls.counter += 1
        return type.__new__(cls,  *args)

    def __init__(cls,  *args):
        cls.class_number = cls.counter - 1


class Cls1(metaclass=Meta):

    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):

    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)

a, b = Cls1('da'), Cls2('ew')

assert (a.class_number, b.class_number) == (0, 1)


# class abstract task
class SerializationInterface():
    def __init__(self):
        self.data = ''

    def serialize(self):
        raise NotImplementedError()
    

class JsonSerialize(SerializationInterface):
    def serialize(self, data_to_ser):
        try:
            self.data = dumps(data_to_ser)
        except TypeError:
            print('We wating for current format')
        return self.data


class BinSerialize(SerializationInterface):
    def serialize(self, data_to_ser):
        self.data = bin_dumps(data_to_ser)
        return self.data


ser_to_json = JsonSerialize()
ser_to_bin = BinSerialize()

ser_to_json.serialize([1,2,23])
ser_to_bin.serialize([1, 2, 3, 4, 5])

print(ser_to_bin.data, ser_to_json.data)
