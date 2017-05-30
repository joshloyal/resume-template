<!-- Education -->
### <i class="fa fa-chevron-right"></i> Education
<table class="table table-hover">
{% for edu in education %}
  <tr>
    <td class="col-md-3">
    <strong>{{ edu.school }}</strong>
    <br>
    {{ edu.degree }}
    {% if edu.gpa %}
      ({{ edu.gpa }})
    {% endif %}
    </td>
    <td>
      <i>{{ edu.location }}</i>
      <br>
      {{ edu.dates }}
    </td>
  </tr>
{% endfor %}
</table>
