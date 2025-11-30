def website():
    def import_file(format):
        with open(f'src/view/index.{format}', 'r') as file:
            return file.read()  # Cambiado a read() para obtener el contenido completo como una cadena

    def pokemon_div(id):
        return(
            '<div class="col-1" style="height: 150px;">'
                f'<div id="poke-bg-{id}">'
                    f'<div id="pk-img-{id}">'
                        f'<h6 id="lvl-{id}" class="lvl"></h6>'
                        f'<h6 id="name-{id}" class="name"></h6>'
                    '</div>'
                '</div>'
            '</div>'
        )

    return (
        '<!DOCTYPE html>'
        '<html lang="es">'
        '<head>'
            '<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            '<title>Overlay</title>'
            '<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">'
            f'<style>{import_file("css")}</style>'
        '</head>'
        '<body>'
            '<div class="container-fluid">'
                '<div class="row">'
                    f'{pokemon_div(0)}'
                    f'{pokemon_div(1)}'
                    f'{pokemon_div(2)}'
                    f'{pokemon_div(3)}'
                    f'{pokemon_div(4)}'
                    f'{pokemon_div(5)}'
                '</div>'
            '</div>'
            f'<script>{import_file("js")}</script>'
        '</body>'
        '</html>'
    )
