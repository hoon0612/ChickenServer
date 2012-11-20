$ ->
#    $('#id_address').after('<button class="btn btn-primary" id="getbtn" > Get </button>')

    update_loc = ->
        address = $('#id_address').val()
        $.get '/geocode/?addr=' + address, (data) ->

            if data == "-1" or data == "-2"
                $('#id_locationX').val('0')
                $('#id_locationY').val('0')
            else
                loc = data.split('/')
                $('#id_locationX').val(loc[0])
                $('#id_locationY').val(loc[1])

        return false

#    $("#getbtn").click(update_loc)
    $("#id_address").change(update_loc)
