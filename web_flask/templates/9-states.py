<HTML lang="en">
    <HEAD>
        <TITLE>HBNB</TITLE>
    </HEAD>
    <BODY>

      {% if states is defined %}
      <H1>States</H1>
      <UL>

        {% for state in states|sort(attribute='name') %}
        <LI>{{ state.id }}: <B>{{ state.name }}</B></LI>
        {% endfor %}

      </UL>
      {% elif state is defined %}
        {% if state == None %}
        <H1>Not found!</H1>
        {% else %}
        <H1>State: {{ state.name }}</H1>
        <H3>Cities:</H3>
        <UL>
          {% for city in state.cities|sort(attribute='name') %}
          <LI>{{ city.id }}: <B>{{ city.name }}</B></LI>
          {% endfor %}
        </UL>
        {% endif %}
      {% endif %}
    </BODY>
</HTML>

