{% extends 'app/base.html' %}

{% block js %}

<script>
    function activarUsuario(id) {
        Swal.fire({
            "title":"¿Estás seguro de activar al usuario?",
            "text":"Este podra acceder al sistema",
            "icon":"question",
            "showCancelButton": true,
            "cancelButtonText":"Cancelar",
            "confirmButtonText":"Aceptar",
            "confirmButtonColor":"#dc3545"
        })
        .then(function(result) {
            if(result.isConfirmed) {
                window.location.href = "/activar-usuario/"+id+"/"
            }
        })
    }
</script>

{% endblock %} 

{% block contenido %}

{% load crispy_forms_tags %}
<br><br><br>
<div class="card" style="margin: 1px 5em;">
        <h3 align="center" >Usuarios Inactivos</h3>
        <table class="table table-sm">
            <tr class="table table-striped table-hover table-responsive-sm">
                <th>Nombre de Usuario</th>
                <th>Estado</th>
                <th>Opción</th>
            </tr>

            {% if object_list %}
            {% for u in object_list %}

            <tr>
                <td>{{u.username | title }}</td>
                <td>
                    {% if u.is_active %}
                    Activa
                    {% else %}
                    Desactivada
                    {% endif %}
                </td>
                <td>
                    <a href="#" onclick="activarUsuario({{ u.id }})" class="btn btn-danger btn-sm">Activar</a>
                </td>         
            </tr>
            {% endfor %}
            {% endif %}
        </table>
</div>


<br><br><br><br><br><br><br><br><br><br>
{% endblock %}
