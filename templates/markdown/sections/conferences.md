<!-- Conferences -->
### <i class="fa fa-chevron-right"></i> Conference Activity & Participation
<table class="table table-hover">
{% for conf in conferences %}
<tr>
<td class="col-md-3">
<strong>{{ conf.title }}</strong><br>
{{ conf.type }} at {{ conf.location }}<br>
{{ conf.event }}, {{ conf.year }}<br>
<!-- {% if conf.code %}[code]({{ conf.code }}){% endif %} -->
{% if conf.code %}[<a href="{{conf.code}}">code</a>]{% endif %}
</td>
</tr>
{% endfor %}
</table>
