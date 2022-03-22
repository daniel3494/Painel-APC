import plotly.express as px
import plotly.graph_objects as go

fig =go.Figure(go.Sunburst(
    labels=["Lucros", "Soja", "Milho em Grãos", "Cana-de-Açúcar", "Café", "Algodão herbáceo", "Arroz", "Laranja", "Mais de R$ 50.000.000", "Menos de R$ 50.000.000"],
    parents=["", "Mais de R$ 50.000.000", "Mais de R$ 50.000.000", "Mais de R$ 50.000.000", "Menos de R$ 50.000.000", "Menos de R$ 50.000.000", "Menos de R$ 50.000.000", "Menos de R$ 50.000.000", "Lucros", "Lucros"],
    values=[10, 169100228, 73949252, 60800886 , 27254184, 19127892, 11631701, 10898251, 169100228 + 73949252 + 60800886, 27254184 + 19127892 + 11631701 + 10898251],
))
fig.update_layout(margin = dict(t=50, l=0, r=0, b=0))

fig.show()