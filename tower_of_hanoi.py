"""Tower of Hanoi."""

class Pole(object):
    def __init__(self):
        self.disks = []

    def addDisk(self, newDisk):
        if len(self.disks) > 0:
            disk_on_top = self.disks[-1]
            if newDisk.data > disk_on_top.data:
                print "Error.  Cannot place larger disk on smaller one."
                print "tried to move %d on top of %d." % (newDisk.data, disk_on_top.data)
                return
        self.disks.append(newDisk)

    def removeDisk(self):
        top_disk = self.disks.pop(-1)
        return top_disk

    def bottom_to_top(self):
        return [disk.data for disk in self.disks]




class Disk(object):
    def __init__(self, data=None):
        self.data = data



# create poles
fromPole = Pole()
withPole = Pole()
toPole = Pole()


# create Disks, and add to original fromPole
fromPole.addDisk(Disk(3))
fromPole.addDisk(Disk(2))
fromPole.addDisk(Disk(1))
print fromPole.bottom_to_top()






def move_disks(fromPole, withPole, toPole):
    # base case.  fromPole has no disks
    if len(fromPole.disks) == 0:
        return toPole

    # move top 2 discs to the middle pole (withPole)
    disk1 = fromPole.removeDisk()
    toPole.addDisk(disk1)

    disk2 = fromPole.removeDisk()
    withPole.addDisk(disk2)

    disk1 = toPole.removeDisk()
    withPole.addDisk(disk1)

    # move the third disk to the last pole (toPole)
    disk3 = fromPole.removeDisk()
    toPole.addDisk(disk3)

    # move the first and second disks on top of the third pole too.  but in order (3rd on bottom, then 2nd, then 1st).
    disk1 = withPole.removeDisk()
    fromPole.addDisk(disk1)

    disk2 = withPole.removeDisk()
    toPole.addDisk(disk2)

    disk1 = fromPole.removeDisk()
    toPole.addDisk(disk1)

    # recursive call, feeding in updated states (poles)
    return move_disks(fromPole, withPole, toPole)




updated_toPole = move_disks(fromPole, withPole, toPole)
print updated_toPole.bottom_to_top()

