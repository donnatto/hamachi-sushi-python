from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 5242880:
        raise ValidationError('El tamaño máximo permitido es de 5MB')
    else:
        return value