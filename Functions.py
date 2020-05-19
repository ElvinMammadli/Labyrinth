from Heap_functions import BinaryHeap


def bfs_stack(start, end_point):
    neighbour_list = []
    traveled_list = []
    readCount= 0
    writeCount = 0
    tmp = [start, 0]
    traveled_list.append(tmp)
    writeCount = writeCount + 1
    total = None
    while True:

        if traveled_list is []:
            total = False
            break

        point = traveled_list.pop(0)[0]
        readCount= readCount+ 1
        k = point
        if isEqual(point, end_point):
            total = True
            break

        point.add_child()

        for worked_point in point.childs:
            if (not isInListOpen(worked_point, traveled_list)) and (not search_neighbour(worked_point, neighbour_list)):
                tmp = []
                worked_point.add_parent(point)
                distance_points = worked_point.distance_pointsTo(end_point)

                worked_point.distance_between_start = worked_point.getParent().distance_between_start
                if worked_point.find_red() == 0:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1
                else:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1.0 / worked_point.find_red()

                tmp.append(worked_point)
                tmp.append(distance_points)
                traveled_list.append(tmp)
                writeCount = writeCount + 1
        traveled_list.sort(key=lambda x: x[1])

        neighbour_list.append(point)

    end_point = k
    return end_point, readCount, writeCount


def bfs_heap(start, end_point):
    neighbour_list = []
    traveled_list = BinaryHeap()
    readCount= 0
    writeCount = 0
    tmp = [start, 0]
    traveled_list.add(tmp)
    writeCount = writeCount + 1
    total = None
    k = None
    while True:

        if traveled_list.isEmpty():
            total = False
            break

        # get minimum point from list and remove from list
        point = traveled_list.extract_min()[0]
        readCount= readCount+ 1
        k = point
        if isEqual(point, end_point):
            break

        point.add_child()

        for worked_point in point.childs:
            if (not search_heap(worked_point, traveled_list)) and (not search_neighbour(worked_point, neighbour_list)):
                tmp = []
                worked_point.add_parent(point)
                distance_points = worked_point.distance_pointsTo(end_point)

                worked_point.distance_between_start = worked_point.getParent().distance_between_start
                if worked_point.find_red() == 0:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1
                else:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1.0 / worked_point.find_red()

                tmp.append(worked_point)
                tmp.append(distance_points)
                traveled_list.add(tmp)
                writeCount = writeCount + 1
        neighbour_list.append(point)

    end_point = k

    return end_point, readCount, writeCount


def as_stack(start, end_point):
    neighbour_list = []
    traveled_list = []
    readCount= 0
    writeCount = 0
    tmp = [start, 0]
    traveled_list.append(tmp)
    writeCount = writeCount + 1
    total = None
    k = None
    while True:

        if traveled_list is []:
            total = False
            break

        # get minimum point from list and remove from list
        point = traveled_list.pop(0)[0]
        readCount= readCount+ 1
        k = point
        if isEqual(point, end_point):
            total = True
            break

        point.add_child()

        for worked_point in point.childs:
            if (not isInListOpen(worked_point, traveled_list)) and (not search_neighbour(worked_point, neighbour_list)):
                tmp = []
                worked_point.add_parent(point)
                distance_points = worked_point.distance_pointsTo(end_point)
                worked_point.distance_between_start = worked_point.getParent().distance_between_start
                if worked_point.find_red() == 0:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1
                else:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1.0 / worked_point.find_red()

                distance_points = distance_points + worked_point.distance_between_start

                tmp.append(worked_point)
                tmp.append(distance_points)
                traveled_list.append(tmp)
                writeCount = writeCount + 1

        traveled_list.sort(key=lambda x: x[1])
        neighbour_list.append(point)
    end_point = k
    return end_point, readCount, writeCount


def as_heap(start, end_point):
    neighbour_list = []
    traveled_list = BinaryHeap()
    readCount= 0
    writeCount = 0
    tmp = [start, 0]
    traveled_list.add(tmp)
    writeCount = writeCount + 1
    total = None
    k = None
    while True:

        if traveled_list.isEmpty():
            total = False
            break

        # get minimum point from list and remove from list
        point = traveled_list.extract_min()[0]
        readCount= readCount+ 1
        k = point
        if isEqual(point, end_point):
            break

        point.add_child()

        for worked_point in point.childs:
            if (not search_heap(worked_point, traveled_list)) and (not search_neighbour(worked_point, neighbour_list)):
                tmp = []
                worked_point.add_parent(point)
                distance_points = worked_point.distance_pointsTo(end_point)

                worked_point.distance_between_start = worked_point.getParent().distance_between_start
                if worked_point.find_red() == 0:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1
                else:
                    worked_point.distance_between_start = worked_point.distance_between_start + 1.0 / worked_point.find_red()
                distance_points = distance_points + worked_point.distance_between_start

                tmp.append(worked_point)
                tmp.append(distance_points)
                traveled_list.add(tmp)
                writeCount = writeCount + 1
        neighbour_list.append(point)

    end_point = k

    return end_point, readCount, writeCount


def search_heap(point, heap):
    for i in heap.items:
        if i[0].x == point.x and i[0].y == point.y:
            return True
    return False


def search_neighbour(point, list2):
    for i in list2:
        if i.x == point.x and i.y == point.y:
            return True
    return False


def isInListOpen(point, list2):
    for i in list2:
        if i[0].x == point.x and i[0].y == point.y:
            return True
    return False


def isEqual(point1, point2):
    return point1.x == point2.x and point1.y == point2.y
