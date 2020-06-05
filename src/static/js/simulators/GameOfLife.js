function createBoard(sizeX, sizeY) {
    const board = []
    for (let i = 0; i < sizeX; i++) {
        board.push([])
        for (let j = 0; j < sizeY; j++) {
            board[i].push(false)
        }
    }
    return asData(board)
}

function createRandomBoard(sizeX, sizeY, aliveProba = .1) {
    const board = []
    for (let i = 0; i < sizeX; i++) {
        board.push([])
        for (let j = 0; j < sizeY; j++) {
            board[i].push(Math.random() < aliveProba)
        }
    }
    return asData(board)
}

function isInbound(x, y, sizeX, sizeY) {
    return x > -1 && x < sizeX && y > -1 && y < sizeY
}

function neighborCountStatus(board, i, j, status = undefined, bounded = false) {
    const sizeY = board.length
    const sizeX = board[0].length

    let counter = 0
    for (const [di, dj] of [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]) {
        if (bounded && !isInbound(i + di, j + dj, size, size))
            continue

        const neighI = (i + di + sizeX) % sizeX
        const neighJ = (j + dj + sizeY) % sizeY
        if (status === undefined || board[neighI][neighJ] === status)
            counter++
    }
    return counter
}

function lives(board, i, j, bounded = false) {
    const neighborsAlive = neighborCountStatus(board, i, j, true, bounded)

    if (board[i][j] === true) {
        if (neighborsAlive === 2 || neighborsAlive === 3) return true
        else return false
    } else {
        if (neighborsAlive === 3) return true
        else return false
    }
}

function evolve(data, bounded = false) {
    const board = asBoard(data)
    return asData(board.map((row, i) => row.map((_, j) => lives(board, i, j, bounded))))

}

function asBoard(data) {
    return data.map(row => row.map(cell => cell.alive))

}


function asData(board) {
    return board.map((row, i) => row.map((cell, j) => {
        return {
            i,
            j,
            alive: cell
        }
    }))
}
