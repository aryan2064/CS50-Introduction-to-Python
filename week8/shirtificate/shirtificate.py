from fpdf import FPDF, Align

def main():
    name = input("Name: ")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("helvetica", style="", size=45)
    pdf.cell(h=40, text="CS50 Shirtificate", center=True)

    pdf.image("./shirtificate.png", x=Align.C, y=60, w=185, keep_aspect_ratio=True)

    pdf.set_font("helvetica", style="", size=25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(h=230, text=f"{name.title()} took CS50", center=True)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
