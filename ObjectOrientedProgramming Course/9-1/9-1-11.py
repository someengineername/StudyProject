class Selfie:
    dict_vault = []

    def save_state(self):
        self.__class__.dict_vault.append(self.__dict__.copy())

    def recover_state(self, index):

        if index in range(len(self.__class__.dict_vault)):

            new_instance = self.__class__()
            new_instance.__dict__.update(self.__class__.dict_vault[index])
            self.__class__.dict_vault = self.__class__.dict_vault[:index]
            return new_instance
        else:
            return self

    def n_states(self):
        return len(self.__class__.dict_vault)