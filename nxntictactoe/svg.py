
import xml.etree.ElementTree as ET


PIECE_SIZE = 30
PIECES = {
"-": """
    <g></g>
""",
"x": """
    <g viewbox="0 0 30 30">
        <line x1="3" y1="3" x2="27" y2="27" stroke="red" stroke-width="3" fill="none" />
        <line x1="3" y1="27" x2="27" y2="3" stroke="red" stroke-width="3" fill="none" />
    </g>
""",
"o": """
    <g viewbox="0 0 30 30">
        <circle cx="15" cy="15" r="12" stroke="blue" stroke-width="3" fill="none" />
    </g>
""",
"t": """
    <g viewbox="0 0 30 30">
        <line x1="3" y1="27" x2="15" y2="3" stroke-linecap="round" stroke="green" stroke-width="3" fill="none" />
        <line x1="15" y1="3" x2="27" y2="27" stroke-linecap="round" stroke="green" stroke-width="3" fill="none" />
        <line x1="3" y1="27" x2="27" y2="27" stroke-linecap="round" stroke="green" stroke-width="3" fill="none" />
    </g>
""",
}
PLAYER_PIECE = ["-", "x", "o", "t"]

def create_svg(w=400, h=400):
    svg = ET.Element("svg", {
        "xmlns": "http://www.w3.org/2000/svg",
        "version": "1.1",
        "xmlns:xlink": "http://www.w3.org/1999/xlink",
        "viewBox": "0 0 %d %d" % (w, h),
        "width": str(w),
        "height": str(h),
    })
    return svg

def create_rect(x, y, w=PIECE_SIZE, h=PIECE_SIZE):
    rect = ET.Element("rect", {
        "x": str(x),
        "y": str(y),
        "width": str(w),
        "height": str(h),
        "fill": "none",
        "stroke": "black",
        "stroke-width": "1"
    })
    return rect

def draw_board(board):
    w = board.cols * PIECE_SIZE
    h = board.rows * PIECE_SIZE
    win_cells = board.get_win_cells()
    svg = create_svg(w, h)
    for row in range(board.rows):
        for col in range(board.cols):
            y = row * PIECE_SIZE
            x = col * PIECE_SIZE
            rect = create_rect(x, y)
            if (row, col) in win_cells:
                rect.set("fill", "#ffff66")  # yellow
            svg.append(rect)
            player_id = board.get(row, col)
            if player_id != board.BLANK:
                piece = ET.fromstring(PIECES[PLAYER_PIECE[player_id]])
                piece.set("transform", "translate({}, {})".format(x, y))
                svg.append(piece)
    return ET.tostring(svg).decode("utf-8")
