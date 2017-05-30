<!-- Work & Research Experience -->
### <i class="fa fa-chevron-right"></i> Work & Research Experience
<table class="table table-hover">
{% for job in work %}
    <tr>
        <td class="col-md-3">
            <strong>{{ job.company }}</strong>
            {% if job.website %}
            <a href="{{ job.website }}">
                <i class="fa fa-link"></i>
            </a>
            {% endif %}<br>
            <i>{{ job.title }}</i>
        </td>
        <td>
            <strong>{{ job.location }}</strong><br>
            <i>{{ job.dates }}</i>
        </td>
    </tr>

    <tr>
        <td colspan="2">
            {% for detail in job.details %}
            <ul>
                <h4><strong>{{ detail.title }}</strong></h4>
                {% for desc in detail.details %}
                    <li>{{ desc }}</li>
                {% endfor %}
            </ul>
            {% endfor %}
        </td>
    </tr>
{% endfor %}
</table>
