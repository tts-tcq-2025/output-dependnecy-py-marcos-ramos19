from tshirts import size
import misaligned
from Weatherreport import report
import io, contextlib
import alerter

# tshirts
def test_tshirts_boundary_38():
    out = size(38)
    assert out in ('S', 'M'), f"size(38) debería ser S o M, salió: {out}"

# misaligned
def _capture_color_map_lines():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        misaligned.print_color_map()
    return buf.getvalue().strip().splitlines()

def test_misaligned_starts_at_1():
    lines = _capture_color_map_lines()
    assert lines[0].startswith("1 | "), f"Primera línea: {lines[0]}"

def test_misaligned_pipe_alignment():
    lines = _capture_color_map_lines()
    pipe_positions = [ln.find('|') for ln in lines]
    assert len(set(pipe_positions)) == 1, f"'|' desalineado: {pipe_positions[:10]}..."

# weatherreport
def _stub_heavy_rain_low_wind():
    return {'temperatureInC': 50, 'precipitation': 70, 'humidity': 10, 'windSpeedKMPH': 10}

def _stub_boundary_precip_60_low_wind():
    return {'temperatureInC': 50, 'precipitation': 60, 'humidity': 10, 'windSpeedKMPH': 0}

def test_weather_heavy_rain_should_not_be_sunny():
    w = report(_stub_heavy_rain_low_wind)
    assert "rain" in w.lower(), f"Lluvia fuerte → esperado 'rain', salió: {w}"

def test_weather_precip_60_should_not_be_sunny():
    w = report(_stub_boundary_precip_60_low_wind)
    assert "rain" in w.lower(), f"Precip=60 → esperado 'rain', salió: {w}"

# alerter
def test_alerter_counts_failures():
    alerter.alert_failure_count = 0
    def failing_sender(_c): return 500
    alerter.alert_in_celcius(400.5, send=failing_sender)
    assert alerter.alert_failure_count == 1, f"Contador: {alerter.alert_failure_count}"

if __name__ == '__main__':
    test_tshirts_boundary_38()
    test_misaligned_starts_at_1()
    test_misaligned_pipe_alignment()
    test_weather_heavy_rain_should_not_be_sunny()
    test_weather_precip_60_should_not_be_sunny()
    test_alerter_counts_failures()
