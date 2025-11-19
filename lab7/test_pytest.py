from app import Figure

def test_app_triangle():
    """Test if we create triangle figure."""
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig, f"Фігура має бути {fig}"
