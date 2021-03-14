class CoordError(Exception):
    pass

class ImageYIter:
    def __init__(self, img):
        self.__img = img
        self.__limit = img.height
        self.__y = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.__y >= self.__limit:
            raise StopIteration

        self.__y += 1
        return ImageXIter(self.__img, self.__y - 1)



class ImageXIter:
    def __init__(self, img, y:int):
        self.__img = img
        self.__limit = img.width
        self.__y = y
        self.__x = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        return self.__img[self.__x-1, self.__y]

class Image:
    def __init__(self, width, height, background = '_'):
        self.__background = background
        self.__pixels = {}
        self.__width = width
        self.__height = height
        self.__colors = set(self.__background)


    @property
    def width(self):
        return self.__width


    @width.setter
    def width(self, width):
        self.__width = width


    @property
    def height(self):
        return self.__height


    @height.setter
    def height(self, height):
        self.__height = height





    def __checkCoords(self, coord):
        if not isinstance(coord, tuple) and len(coord) != 2:
            raise CoordError('Please enter 2 - lenght tuple')
        if not (0 <= coord[0] <= self.__width) or not (0 <= coord[1] <= self.__height):
            raise CoordError('Entered points are out of range')



    def __setitem__(self, coord, color):
        self.__checkCoords(coord)

        if color == self.__background:
            self.__pixels.pop(coord, None)
        else:
            self.__pixels[coord] = color
            self.__colors.add(color)


    def __getitem__(self, coord):
        self.__checkCoords(coord)
        return self.__pixels.get(coord, self.__background)


    def __iter__(self):
        return ImageYIter(self)



    def resize(self, newWidth = None, newHeight = None):
        if newHeight is None and newWidth is None:
            self.height = self.height
            self.width = self.width
        elif newHeight is None:
            self.height = self.height
            self.width = newWidth
        elif newWidth is None:
            self.width = self.width
            self.height = newHeight
        else:
            self.height = newHeight
            self.width  = newWidth
           # return self.__init__(newWidth, newHeight)


img = Image(20, 4)
for i in range(4):
    for j in range(10):
        img[(j, i)] = '*'
img[(1, 1)] = '*' ; img[(2, 1)] = '*' ; img[(3, 1)] = '*'
img.resize(25, 8)
for raw in img:
    for y in raw:
        print(y, sep='', end='')
    print()

print('#' * 20)

#img.resize(25, 8)


# for raw in img:
#     for y in raw:
#         print(y, sep='', end='')
#     print()

# print('#' * 20)

# img.resize(10)


# for raw in img:
#     for y in raw:
#         print(y, sep='', end='')
#     print()
