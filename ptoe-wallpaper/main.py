#command line: manimgl main.py ptoe -c #101318
from manimlib import *
cnname = ['氢', '氦', '锂', '铍', '硼', '碳', '氮', '氧', '氟', '氖', '钠', '镁', '铝', '硅', '磷', '硫', '氯', '氩', '钾', '钙', '钪', '钛', '钒', '铬', '锰', '铁', '钴', '镍', '铜', '锌', '镓', '锗', '砷', '硒', '溴', '氪', '铷', '锶', '钇', '锆', '铌', '钼', '锝', '钌', '铑', '钯', '银', '镉', '铟', '锡', '锑', '碲', '碘', '氙', '铯', '钡', '镧', '铈', '镨', '钕', '钷', '钐', '铕', '钆', '铽', '镝', '钬', '铒', '铥', '镱', '镥', '铪', '钽', '钨', '铼', '锇', '铱', '铂', '金', '汞', '铊', '铅', '铋', '钋', '砹', '氡', '钫', '镭', '锕', '钍', '镤', '铀', '镎', '钚', '镅', '锔', '锫', '锎', '锿', '镄', '钔', '锘', '铹', '𬬻', '𬭊', '𬭳', '𬭛', '𬭶', '鿏', '𫟼', '𬬭', '鿔', '鿭', '𫓧', '镆', '𫟷', '鿬', '鿫']

enname = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Flourine', 'Neon', 'Sodium', 'Magnesium', 'Aluminium', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium', 'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper', 'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium', 'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium', 'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Caesium', 'Barium', 'Lanthanum', 'Cerium', 'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium', 'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium', 'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine', 'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium', 'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium', 'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium', 'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson']

symbol = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

atomic_mass = ['1.008', '4.0026', '6.94', '9.0122', '10.81', '12.011', '14.007', '15.999', '18.998', '20.18', '22.99', '24.305', '26.982', '28.085', '30.974', '32.06', '35.45', '39.948', '39.098', '40.078', '44.956', '47.867', '50.942', '51.996', '54.938', '55.845', '58.933', '58.693', '63.546', '65.38', '69.723', '72.63', '74.922', '78.971', '79.904', '83.798', '85.468', '87.62', '88.906', '91.224', '92.906', '95.95', '(98)', '101.07', '102.91', '106.42', '107.87', '112.41', '114.82', '118.711', '121.76', '127.6', '126.9', '131.29', '132.91', '137.33', '138.91', '140.12', '140.91', '144.24', '144.24', '150.36', '151.96', '157.25', '158.93', '162.5', '164.93', '167.26', '168.93', '173.05', '174.97', '178.49', '180.95', '183.84', '186.21', '190.23', '192.22', '195.08', '196.97', '200.59', '204.38', '207.2', '208.98', '(209)', '(210)', '(222)', '(223)', '(226)', '(227)', '232.04', '231.04', '238.03', '(237)', '(244)', '(243)', '(247)', '(247)', '(251)', '(252)', '(257)', '(258)', '(259)', '(266)', '(267)', '(268)', '(269)', '(270)', '(277)', '(278)', '(281)', '(282)', '(282)', '(286)', '(289)', '(290)', '(293)', '(294)', '(294)']

atomic_weight = [[1], [2], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 8, 1], [2, 8, 2], [2, 8, 3], [2, 8, 4], [2, 8, 5], [2, 8, 6], [2, 8, 7], [2, 8, 8], [2, 8, 8, 1], [2, 8, 8, 2], [2, 8, 9, 2], [2, 8, 10, 2], [2, 8, 11, 2], [2, 8, 13, 1], [2, 8, 13, 2], [2, 8, 14, 2], [2, 8, 15, 2], [2, 8, 16, 2], [2, 8, 18, 1], [2, 8, 18, 2], [2, 8, 18, 3], [2, 8, 18, 4], [2, 8, 18, 5], [2, 8, 18, 6], [2, 8, 18, 7], [2, 8, 18, 8], [2, 8, 18, 8, 1], [2, 8, 18, 8, 2], [2, 8, 18, 9, 2], [2, 8, 18, 10, 2], [2, 8, 18, 12, 1], [2, 8, 18, 13, 1], [2, 8, 18, 13, 2], [2, 8, 18, 15, 1], [2, 8, 18, 16, 1], [2, 8, 18, 18], [2, 8, 18, 18, 1], [2, 8, 18, 18, 2], [2, 8, 18, 18, 3], [2, 8, 18, 18, 4], [2, 8, 18, 18, 5], [2, 8, 18, 18, 6], [2, 8, 18, 18, 7], [2, 8, 18, 18, 8], [2, 8, 18, 18, 8, 1], [2, 8, 18, 18, 8, 2], [2, 8, 18, 18, 9, 2], [2, 8, 18, 19, 9, 2], [2, 8, 18, 21, 8, 2], [2, 8, 18, 22, 8, 2], [2, 8, 18, 23, 8, 2], [2, 8, 18, 24, 8, 2], [2, 8, 18, 25, 8, 2], [2, 8, 18, 25, 9, 2], [2, 8, 18, 27, 8, 2], [2, 8, 18, 28, 8, 2], [2, 8, 18, 29, 8, 2], [2, 8, 18, 30, 8, 2], [2, 8, 18, 31, 8, 2], [2, 8, 18, 32, 8, 2], [2, 8, 18, 32, 9, 2], [2, 8, 18, 32, 10, 2], [2, 8, 18, 32, 11, 2], [2, 8, 18, 32, 12, 2], [2, 8, 18, 32, 13, 2], [2, 8, 18, 32, 14, 2], [2, 8, 18, 32, 15, 2], [2, 8, 18, 32, 17, 1], [2, 8, 18, 32, 18, 1], [2, 8, 18, 32, 18, 2], [2, 8, 18, 32, 18, 3], [2, 8, 18, 32, 18, 4], [2, 8, 18, 32, 18, 5], [2, 8, 18, 32, 18, 6], [2, 8, 18, 32, 18, 7], [2, 8, 18, 32, 18, 8], [2, 8, 18, 32, 18, 8, 1], [2, 8, 18, 32, 18, 8, 2], [2, 8, 18, 32, 18, 9, 2], [2, 8, 18, 32, 18, 10, 2], [2, 8, 18, 32, 20, 9, 2], [2, 8, 18, 32, 21, 9, 2], [2, 8, 18, 32, 22, 9, 2], [2, 8, 18, 32, 24, 8, 2], [2, 8, 18, 32, 25, 8, 2], [2, 8, 18, 32, 25, 9, 2], [2, 8, 18, 32, 27, 8, 2], [2, 8, 18, 32, 28, 8, 2], [2, 8, 18, 32, 29, 8, 2], [2, 8, 18, 32, 30, 8, 2], [2, 8, 18, 32, 31, 8, 2], [2, 8, 18, 32, 32, 8, 2], [2, 8, 18, 32, 32, 8, 3], [2, 8, 18, 32, 32, 10, 2], [2, 8, 18, 32, 32, 11, 2], [2, 8, 18, 32, 32, 12, 2], [2, 8, 18, 32, 32, 13, 2], [2, 8, 18, 32, 32, 14, 2], [2, 8, 18, 32, 32, 15, 2], [2, 8, 18, 32, 32, 17, 1], [2, 8, 18, 32, 32, 17, 2], [2, 8, 18, 32, 32, 18, 2], [2, 8, 18, 32, 32, 18, 3], [2, 8, 18, 32, 32, 18, 4], [2, 8, 18, 32, 32, 18, 5], [2, 8, 18, 32, 32, 18, 6], [2, 8, 18, 32, 32, 18, 7], [2, 8, 18, 32, 32, 18, 8]]

attribute = ['other-nonmetal', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'metalloid', 'other-nonmetal', 'other-nonmetal', 'other-nonmetal', 'other-nonmetal', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'post-transition-metal', 'metalloid', 'other-nonmetal', 'other-nonmetal', 'other-nonmetal', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'post-transition-metal', 'metalloid', 'metalloid', 'other-nonmetal', 'other-nonmetal', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'post-transition-metal', 'post-transition-metal', 'metalloid', 'metalloid', 'other-nonmetal', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'lanthanoid', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'post-transition-metal', 'post-transition-metal', 'post-transition-metal', 'post-transition-metal', 'metalloid', 'noble-gas', 'alkali-metal', 'alkaline-earth-metal', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'actinoid', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'transition-metal', 'unknown', 'unknown', 'unknown', 'transition-metal', 'unknown', 'post-transition-metal', 'unknown', 'unknown', 'unknown', 'unknown']

cnattribute = ["碱金属", "碱土金属", "镧系元素", "锕系元素", "过渡金属", "后过渡金属", "类金属", "其他非金属", "稀有气体", "未知元素"]

colors = {
    "background" : "#101318",
    "alkali-metal" : "#ecbe59",
    "alkaline-earth-metal" : "#dee955",
    "lanthanoid" : "#ec77a3",
    "actinoid" : "#c686cc",
    "transition-metal" : "#fd8572",
    "post-transition-metal" : "#4cddf3",
    "metalloid" : "#3aefb6",
    "other-nonmetal" : "#52ee61",
    "noble-gas" : "#759fff",
    "unknown" : "#cccccc"
}

position = [(0, 0), (17, 0), (0, 1), (1, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1), (0, 2), (1, 2), (12, 2), (13, 2), (14, 2), (15, 2), (16, 2), (17, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (12, 3), (13, 3), (14, 3), (15, 3), (16, 3), (17, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4), (10, 4), (11, 4), (12, 4), (13, 4), (14, 4), (15, 4), (16, 4), (17, 4), (0, 5), (1, 5), (1.5, 8), (2.5, 8), (3.5, 8), (4.5, 8), (5.5, 8), (6.5, 8), (7.5, 8), (8.5, 8), (9.5, 8), (10.5, 8), (11.5, 8), (12.5, 8), (13.5, 8), (14.5, 8), (15.5, 8), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (11, 5), (12, 5), (13, 5), (14, 5), (15, 5), (16, 5), (17, 5), (0, 6), (1, 6), (1.5, 9), (2.5, 9), (3.5, 9), (4.5, 9), (5.5, 9), (6.5, 9), (7.5, 9), (8.5, 9), (9.5, 9), (10.5, 9), (11.5, 9), (12.5, 9), (13.5, 9), (14.5, 9), (15.5, 9), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6), (10, 6), (11, 6), (12, 6), (13, 6), (14, 6), (15, 6), (16, 6), (17, 6), (2, 5), (2, 6)]



class PTOE(Scene):
    def construct(self) -> None:
        ennames = [
            Text(enname[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.4).shift(DOWN*1.5)
            for i in range(118)
        ]
        ennames.append(Text("Lanthanoid", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.4).shift(DOWN*1.5))
        ennames.append(Text("Actinoid", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.4).shift(DOWN*1.5))
        center = [
            Group(
                    Square(side_length=5, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors[attribute[i]]),
                    Text(cnname[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=2.5),
                    ennames[i],
                    Text(atomic_mass[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.4).shift(DOWN*2),
                    Text(str(i+1), font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.5).next_to(Square(side_length=4, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UL),
                    Text(symbol[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.5).next_to(Square(side_length=4, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UR)
                )
            for i in range(118)
        ]
        lanthanoid = Group(
                    Square(side_length=5, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors["lanthanoid"]),
                    Text("镧系", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=1.2),
                    ennames[-2],
                    Text("57-71", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.5).next_to(Square(side_length=4, fill_color=colors["lanthanoid"], fill_opacity=0.1, stroke_color=colors["lanthanoid"]), ORIGIN, aligned_edge=UL),
                    Text("La-Lu", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.5).next_to(Square(side_length=4, fill_color=colors["lanthanoid"], fill_opacity=0.1, stroke_color=colors["lanthanoid"]), ORIGIN, aligned_edge=UR)
        )
        actinoid = Group(
                    Square(side_length=5, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors["actinoid"]),
                    Text("锕系", font="Source Han Sans SC", fill_color=colors["actinoid"], height=1.2),
                    ennames[-1],
                    Text("89-103", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.5).next_to(Square(side_length=4, fill_color=colors["actinoid"], fill_opacity=0.1, stroke_color=colors["actinoid"]), ORIGIN, aligned_edge=UL),
                    Text("Ac-Lr", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.5).next_to(Square(side_length=4, fill_color=colors["actinoid"], fill_opacity=0.1, stroke_color=colors["actinoid"]), ORIGIN, aligned_edge=UR)
        )
        '''table = [
            Group(
                Square(side_length=0.6, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors[attribute[i]]).set_stroke(width=1),
                Text(cnname[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.3),
                Text(atomic_mass[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).shift(DOWN*0.21),
                Text(str(i+1), font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UL),
                Text(symbol[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UR)
            ).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[i][0]*0.7 + DOWN*position[i][1]*0.7)
            for i in range(118)
        ]'''
        for i in range(118):
            self.play(FadeIn(center[i]))
            #self.play(ScaleInPlace(center[i], scale_factor=0.12), center[i].animate.shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[i][0]*0.7 + DOWN*position[i][1]*0.7))
            center[i].generate_target()
            center[i].target.scale(0.12).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[i][0]*0.7 + DOWN*position[i][1]*0.7)
            self.play(MoveToTarget(center[i]))
            self.play(FadeOut(ennames[i]))
            #self.wait()
            if i == 70:
                self.play(TransformFromCopy(Group(center[56], center[57], center[58], center[59], center[60], center[61], center[62], center[63], center[64], center[65], center[66], center[67], center[68], center[69], center[70]), lanthanoid))
                lanthanoid.generate_target()
                lanthanoid.target.scale(0.12).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*2*0.7 + DOWN*5*0.7)
            elif i == 102:
                self.play(TransformFromCopy(Group(center[88], center[89], center[90], center[91], center[92], center[93], center[94], center[95], center[96], center[97], center[98], center[99], center[100], center[101], center[102]), actinoid))
                actinoid.generate_target()
                actinoid.target.scale(0.12).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*2*0.7 + DOWN*6*0.7)

class PTOEImage(Scene):
    def construct(self) -> None:
        '''table = [
            Group(
                Square(side_length=0.6, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors[attribute[i]]).set_stroke(width=1),
                Text(cnname[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.3),
                Text(atomic_mass[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).shift(DOWN*0.21),
                Text(str(i+1), font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UL),
                Text(symbol[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UR)
            ).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[i][0]*0.7 + DOWN*position[i][1]*0.7)
            for i in range(118)
        ]'''
        table = []
        for i in range(118):
            table.append(
                Group(
                    Square(side_length=0.6, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors[attribute[i]]).set_stroke(width=1),
                    Text(cnname[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.3),
                    Text(atomic_mass[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).shift(DOWN*0.21),
                    Text(str(i+1), font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UL),
                    Text(symbol[i], font="Source Han Sans SC", fill_color=colors[attribute[i]], height=0.06).next_to(Square(side_length=0.48, fill_color=colors[attribute[i]], fill_opacity=0.1, stroke_color=colors[attribute[i]]), ORIGIN, aligned_edge=UR)
                ).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[i][0]*0.7 + DOWN*position[i][1]*0.7)
            )
            print("\r", i+1, "/", 118, end="")
        print()
        lanthanoid = Group(
                    Square(side_length=0.6, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors["lanthanoid"]).set_stroke(width=1),
                    Text("镧系", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.2),
                    Text("Lanthanoid", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.06).shift(DOWN*0.21),
                    Text("57-71", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.06).next_to(Square(side_length=0.48, fill_color=colors["lanthanoid"], fill_opacity=0.1, stroke_color=colors["lanthanoid"]), ORIGIN, aligned_edge=UL),
                    Text("La-Lu", font="Source Han Sans SC", fill_color=colors["lanthanoid"], height=0.06).next_to(Square(side_length=0.48, fill_color=colors["lanthanoid"], fill_opacity=0.1, stroke_color=colors["lanthanoid"]), ORIGIN, aligned_edge=UR)
        ).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[-2][0]*0.7 + DOWN*position[-2][1]*0.7)
        actinoid = Group(
                    Square(side_length=0.6, fill_color=colors["background"], fill_opacity=0.2, stroke_color=colors["actinoid"]).set_stroke(width=1),
                    Text("锕系", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.2),
                    Text("Actinoid", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.06).shift(DOWN*0.21),
                    Text("89-103", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.06).next_to(Square(side_length=0.48, fill_color=colors["actinoid"], fill_opacity=0.1, stroke_color=colors["actinoid"]), ORIGIN, aligned_edge=UL),
                    Text("Ac-Lr", font="Source Han Sans SC", fill_color=colors["actinoid"], height=0.06).next_to(Square(side_length=0.48, fill_color=colors["actinoid"], fill_opacity=0.1, stroke_color=colors["actinoid"]), ORIGIN, aligned_edge=UR)
        ).shift(LEFT*5.95 + UP*3.15).shift(RIGHT*position[-1][0]*0.7 + DOWN*position[-1][1]*0.7)
        for i in range(118):
            self.add(table[i])
        self.add(lanthanoid)
        self.add(actinoid)
        self.add(Text("元素周期表", font="Source Han Sans SC", fill_color="#ffffff", height=0.5).shift(TOP + DOWN*0.7))