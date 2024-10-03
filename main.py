class Consts:
    DEFAULT = "default"
    YES = "y"
    NO = "n"
    EXIT = "e"
    VAULTS = "Своды"
    ARCHS = "Арочные своды"
    HIGH = "Высокие своды"
    VAULTED_CEILING = "Сводчатый потолок"
    WINDOWS = "Окна"
    STAINED_GLASS = "Витражи"
    RIBBON_GLAZING = "Ленточное остекление"
    HIGH_WINDOWS_WITH_SHALLOW_GLAZING = "Высокие окна с мелкой расстекловкой"
    ROSE_WINDOW = "Окно-роза"
    STYLE = "Стиль"
    GOTHIC = "Готика"
    EMPYRE = "Ампир"
    POINTED_SPIRES = "Остроконечные шпили"
    ARTIFICIAL_MATERIAL = "Искусственный материал"
    NATURAL_MATERIAL = "Натуральный материал"
    HIGH_BUILDING = "Высокое здание"
    MONUMENTALITY = "Монументальность"
    GILDING_IN_DETAIL = "Позолота в деталях"
    MARBLE = "Мрамор"
    WOOD = "Дерево"
    STONE = "Камень"
    CRYSTAL = "Хрусталь"
    CONCRETE = "Бетон"
    METAL = "Металл"
    GLASS = "Стекло"
    EMPHASIS_ON_COLOR_SCHEME = "Акцент на цветовом решении"
    BRIGHT_COLORS = "Яркие тона"
    PASTEL_COLORS = "Пастельные тона"
    CLASSICISM = "Классицизм"
    PROPORTIONALITY = "Пропорциональность"
    SYMMETRY = "Симметричность"
    ANTISYMMETRY = "Асимметричность"
    ANTIQUE_ORDER = "Античный ордер"
    ANTIQUE = "Античный"
    COLUMNS = "Колонны"
    SREREOBAT = "Стереобат"
    MODERN = "Модерн"
    BAROQUE = "Барокко"
    ROCOCO = "Рококо"
    MODERNISM = "Модернизм"
    MOSAIC = "Мозаика"
    SWC_LINES = "Плавные, волнистые, изогнутые линии в декоре фасадов и интерьеров"
    NO_DECOR = "Отсутствие декора"
    EMPHASIS_ON_VOLUME = "Акцент на объем"


class Ask:
    def __init__(self, choices=[Consts.YES, Consts.NO, Consts.EXIT]):
        self.choices = choices

    def ask(self):
        print(f"Введите один из вариантов ответа: {', '.join(self.choices)}")
        return input()


class Content:
    def __init__(self, x):
        self.x = x


class IF(Content):
    pass


class AND(Content):
    pass


class OR(Content):
    pass


rules = {
    Consts.DEFAULT: Ask([Consts.YES, Consts.NO, Consts.EXIT]),
    Consts.VAULTS: IF(AND([Consts.ARCHS, Consts.HIGH, Consts.VAULTED_CEILING])),
    Consts.WINDOWS: Ask(
        [
            Consts.STAINED_GLASS,
            Consts.RIBBON_GLAZING,
            Consts.HIGH_WINDOWS_WITH_SHALLOW_GLAZING,
            Consts.ROSE_WINDOW,
        ]
    ),
    Consts.PROPORTIONALITY: Ask(
        [
            Consts.SYMMETRY,
            Consts.ANTISYMMETRY,
        ]
    ),
    Consts.NATURAL_MATERIAL: IF(
        OR([Consts.MARBLE, Consts.WOOD, Consts.STONE, Consts.CRYSTAL])
    ),
    Consts.ARTIFICIAL_MATERIAL: IF(OR([Consts.CONCRETE, Consts.GLASS, Consts.METAL])),
    Consts.EMPHASIS_ON_COLOR_SCHEME: IF(
        OR([Consts.BRIGHT_COLORS, Consts.PASTEL_COLORS])
    ),
    Consts.ANTIQUE_ORDER: IF(AND([Consts.COLUMNS, Consts.SREREOBAT])),
    f"{Consts.WINDOWS}:{Consts.ROSE_WINDOW},{Consts.STAINED_GLASS}": IF(
        AND([Consts.ROSE_WINDOW, Consts.STAINED_GLASS])
    ),
    f"{Consts.STYLE}:{Consts.GOTHIC}": IF(
        [
            Consts.VAULTS,
            Consts.POINTED_SPIRES,
            f"{Consts.WINDOWS}:{Consts.ROSE_WINDOW},{Consts.STAINED_GLASS}",
            Consts.ARTIFICIAL_MATERIAL,
            Consts.NATURAL_MATERIAL,
            Consts.HIGH_BUILDING,
        ]
    ),
    f"{Consts.STYLE}:{Consts.EMPYRE}": IF(
        [
            Consts.MONUMENTALITY,
            Consts.GILDING_IN_DETAIL,
            Consts.EMPHASIS_ON_COLOR_SCHEME,
        ]
    ),
    f"{Consts.STYLE}:{Consts.CLASSICISM}": IF(
        [
            Consts.NATURAL_MATERIAL,
            Consts.ARTIFICIAL_MATERIAL,
            f"{Consts.PROPORTIONALITY}:{Consts.SYMMETRY}",
            f"{Consts.WINDOWS}:{Consts.HIGH_WINDOWS_WITH_SHALLOW_GLAZING}",
            Consts.ANTIQUE_ORDER,
        ]
    ),
    f"{Consts.STYLE}:{Consts.ANTIQUE}": IF(
        [
            Consts.ARTIFICIAL_MATERIAL,
            Consts.NATURAL_MATERIAL,
            Consts.GILDING_IN_DETAIL,
            Consts.ANTIQUE_ORDER,
        ]
    ),
    f"{Consts.STYLE}:{Consts.MODERN}": IF(
        [
            Consts.MOSAIC,
            Consts.SWC_LINES,


            f"{Consts.WINDOWS}:{Consts.STAINED_GLASS}",
            Consts.NATURAL_MATERIAL,
            Consts.HIGH_BUILDING,
        ]
    ),
    f"{Consts.STYLE}:{Consts.MODERNISM}": IF(
        [
            Consts.NO_DECOR,
            Consts.EMPHASIS_ON_VOLUME,
            f"{Consts.WINDOWS}:{Consts.RIBBON_GLAZING}",
            f"{Consts.PROPORTIONALITY}:{Consts.ANTISYMMETRY}",
        ]
    ),
    f"{Consts.STYLE}:{Consts.BAROQUE}": IF(
        [
            Consts.VAULTS,
            Consts.EMPYRE,
            Consts.ARTIFICIAL_MATERIAL,
            Consts.NATURAL_MATERIAL,
            Consts.GILDING_IN_DETAIL,
            Consts.HIGH_BUILDING,
        ]
    ),
    f"{Consts.STYLE}:{Consts.ROCOCO}": IF(
        [
            Consts.NATURAL_MATERIAL,
            Consts.ARTIFICIAL_MATERIAL,
            f"{Consts.PROPORTIONALITY}:{Consts.ANTISYMMETRY}",
            Consts.MARBLE,
            Consts.WOOD,
            Consts.STONE,
            Consts.CRYSTAL,
            Consts.CONCRETE,
            Consts.METAL,
            Consts.GLASS,
            Consts.EMPHASIS_ON_COLOR_SCHEME,
        ]
    )
}


class KnowledgeBase:
    def __init__(self, rules):
        self.rules = rules
        self.memory = {}

    def search(self, name):
        res = self.__get(name)
        if res == Consts.NO:
            return "Не найдено"
        return f"Это {res}"

    def __get(self, name):
        if name in self.memory.keys():
            return self.memory[name]
        if ":" in name:
            if name.count(":") > 1:
                return Consts.NO
            fld, value = name.split(":")
            if fld in self.memory:
                return self.memory[fld]
            if self.rules.get(name, None) is not None:
                return self.eval(self.rules[name], field=value)
            res = self.eval(self.rules[fld], field=fld)
            self.memory[fld] = res
            if value == res:
                return Consts.YES
            return Consts.NO
        default = True
        for fld in self.rules.keys():
            if fld == name or fld.startswith(name + ":"):
                default = False
                if fld == name:
                    value = fld
                else:
                    value = fld.split(":")[1]
                res = self.eval(self.rules[fld], field=name)
                self.memory[name] = res
                if res == Consts.YES:
                    return value
        if not default:
            return Consts.NO
        res = self.eval(self.rules["default"], field=name)
        self.memory[name] = res
        return res

    def eval(self, expr, field=None):
        if isinstance(expr, Ask):
            if field is not None:
                print(f"{field}?")
            res = expr.ask()
            while res not in expr.choices:
                print("Некорректный ввод. Повторите попытку.")
                res = expr.ask()
            if res == Consts.EXIT:
                exit()
            return res
        if isinstance(expr, IF):
            return self.eval(expr.x)
        if isinstance(expr, AND) or isinstance(expr, list):
            expr = expr.x if isinstance(expr, AND) else expr
            for x in expr:
                if self.eval(x) == Consts.NO:
                    return Consts.NO
            return Consts.YES
        if isinstance(expr, OR):
            for x in expr.x:
                if self.eval(x) == Consts.YES:
                    return Consts.YES
            return Consts.NO
        if isinstance(expr, str):
            return self.__get(expr)
        print("Unknown expr: {}".format(expr))


if __name__ == "__main__":
    while True:
        print("Отвечайте y или n, чтобы определить стиль здания")
        print("Введите e, если хотите прекратить работу программы")
        kb = KnowledgeBase(rules)
        print(kb.search(Consts.STYLE))
        print()
