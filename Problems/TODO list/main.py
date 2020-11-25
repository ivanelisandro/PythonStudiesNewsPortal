template = """
<html>
  <ul>
  {% for activity in todos %}
    <li> {{ activity }} </li>
  {% endfor %}
  </ul>
</html>
"""
