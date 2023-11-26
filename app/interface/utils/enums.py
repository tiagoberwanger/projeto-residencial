from enum import Enum


class RoomEnum(Enum):
    ROOM = 'quarto'
    STUDIO = 'quitinete'
    APARTMENT = 'apartamento'


class StatusEnum(Enum):
    ACTIVE = 'ativo'
    ENDED = 'finalizado'
    RENEWED = 'renovado'
