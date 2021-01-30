from odmantic import Field, Model, EmbeddedModel, AIOEngine


class Guild(Model):
    id: int
    name: str
