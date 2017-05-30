<!-- Teaching Experience -->
### <i class="fa fa-chevron-right"></i> Teaching Experience
<table class="table table-hover">
{% for job in teaching %}
    <tr>
        <td class="col-md-3">
            <strong>{{ job.company }}</strong><br>
            <i>{{ job.title }}</i>
        </td>
        <td>
            <strong>{{ job.location }}</strong><br>
            <i>{{ job.dates }}</i>
        </td>
    </tr>

    <tr>
        <td colspan="2">
        <ul>
            <li>{{ job.details }}</li>
        </ul>
        </td>
    </tr>
{% endfor %}
</table>
