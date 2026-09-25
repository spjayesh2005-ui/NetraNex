from PIL import Image

SEVERITY_LEVELS = [
    ("No DR", "Low"),
    ("Mild DR", "Moderate"),
    ("Moderate DR", "Moderate"),
    ("Severe DR", "High"),
    ("Proliferative DR", "High"),
]

def demo_predict(image: Image.Image):
    # DEMO ONLY: deterministic placeholder based on image dimensions.
    # Replace this with a validated DR model before any real-world use.
    width, height = image.size
    index = (width + height) % len(SEVERITY_LEVELS)
    severity, risk = SEVERITY_LEVELS[index]

    return {
        "mode": "demo",
        "severity": severity,
        "risk": risk,
        "confidence": 0.82,
        "explanation": "Demo result only. A validated clinical model is required for actual screening.",
        "heatmap": None,
        "recommendation": (
            "Continue routine eye screening."
            if risk == "Low"
            else "Consider referral to an eye-care professional for further evaluation."
        ),
    }
