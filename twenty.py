from reportlab.pdfgen import canvas

A4_WIDTH = 210 / 25.4 * 72
A3_WIDTH = 297 / 25.4 * 72
PAGE_WIDTH = A3_WIDTH

NUM_CHARS = 1024
FONT_SIZE = 0.5
STEP = PAGE_WIDTH / float(NUM_CHARS)
MARGIN = STEP / 2
SQUARE_PAGE = (PAGE_WIDTH, PAGE_WIDTH)

GRID = False

sq_canvas = canvas.Canvas("two to the twenty.pdf", pagesize=SQUARE_PAGE)
sq_canvas.setFont("Helvetica", FONT_SIZE)

# GRID just for debugging the placement of the chars
if GRID:
    sq_canvas.setLineWidth(0.01)
    sq_canvas.setFillGray(250)
    for i in range(1, NUM_CHARS + 1):
        sq_canvas.line(0, i * STEP - MARGIN, PAGE_WIDTH, i * STEP - MARGIN)
        sq_canvas.line(i * STEP - MARGIN, 0, i * STEP - MARGIN, PAGE_WIDTH)

sq_canvas.setFillGray(0)

with open("2^20.txt", "r") as twenty_fd:
    for i in range(NUM_CHARS):
        for j in range(NUM_CHARS):
            letter = twenty_fd.readline()[0]  # ignore the LF/CR
            sq_canvas.drawCentredString(
                MARGIN + j * STEP, PAGE_WIDTH - MARGIN - STEP / 4 - i * STEP, letter
            )

sq_canvas.showPage()
sq_canvas.save()
