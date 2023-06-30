def firstBadVersion(self, n: int) -> int:
    l = 1
    r = n

    while(l < r):
        current = l + (r - l) // 2

        bad_version = isBadVersion(current)

        if(bad_version):
            r = current
        else:
            l = current + 1

    return l