def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record_move():
        moves.append(" ".join(str(rod) for rod in rods))

    def move_disks(number, source, target, auxiliary):
        if number == 0:
            return

        move_disks(number - 1, source, auxiliary, target)

        disk = rods[source].pop()
        rods[target].append(disk)
        record_move()

        move_disks(number - 1, auxiliary, target, source)

    record_move()
    move_disks(n, 0, 2, 1)

    return "\n".join(moves)