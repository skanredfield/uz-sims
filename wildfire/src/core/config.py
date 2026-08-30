class Config:

    def __init__(self):
        self.is_deterministic = True
        self.use_von_neumann = True
        self.seed = 12345

    def __form_line(self, name, val):
        return f"{name}:{val}\n"

    def save_config(self):
        lines = [self.__form_line("is_deterministic", "1" if self.is_deterministic else "0")]
        lines.append(self.__form_line("use_von_neumann", "1" if self.use_von_neumann else "0"))
        lines.append(self.__form_line("seed", str(self.seed)))
        with open("wildfire_config.wcfg", "w") as f:
            f.writelines(lines)

    def load_config(self, path):
        with open(path, "r") as f:
           for line in f.readlines():
                name, val = line.replace(" ", "").split(":")
                match(name):
                    case "is_deterministic":
                       self.is_deterministic = True if val == 1 else False
                    case "use_von_neumann":
                        self.use_von_neumann = True if val == 1 else False
                    case "seed":
                        self.seed = int(val)