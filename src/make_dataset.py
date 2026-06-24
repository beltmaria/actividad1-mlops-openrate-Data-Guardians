from pathlib import Path

import numpy as np
import pandas as pd
import yaml


def load_params():
    with open("params.yaml", "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def generate_dataset(n_samples: int, random_state: int) -> pd.DataFrame:
    np.random.seed(random_state)

    user_id = np.arange(1, n_samples + 1)

    site = np.random.choice(
        ["web", "app", "marketplace"],
        size=n_samples
    )

    campaign_type = np.random.choice(
        ["promotion", "reminder", "news", "transactional"],
        size=n_samples
    )

    device_os = np.random.choice(
        ["android", "ios"],
        size=n_samples
    )

    hour_of_day = np.random.randint(0, 24, size=n_samples)

    day_of_week = np.random.choice(
        ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
        size=n_samples
    )

    historical_open_rate = np.round(
        np.random.beta(2, 5, size=n_samples),
        3
    )

    historical_push_count = np.random.randint(1, 80, size=n_samples)

    days_since_last_open = np.random.randint(0, 60, size=n_samples)

    segment = np.random.choice(
        ["new", "active", "inactive", "premium"],
        size=n_samples
    )

    probability = (
        0.15
        + 0.50 * historical_open_rate
        - 0.004 * days_since_last_open
        + 0.08 * (campaign_type == "promotion")
        + 0.06 * (segment == "active")
        + 0.05 * (segment == "premium")
        + 0.04 * ((hour_of_day >= 18) & (hour_of_day <= 21))
    )

    probability = np.clip(probability, 0.01, 0.95)

    target_opened = np.random.binomial(1, probability)

    data = pd.DataFrame(
        {
            "user_id": user_id,
            "site": site,
            "campaign_type": campaign_type,
            "device_os": device_os,
            "hour_of_day": hour_of_day,
            "day_of_week": day_of_week,
            "historical_open_rate": historical_open_rate,
            "historical_push_count": historical_push_count,
            "days_since_last_open": days_since_last_open,
            "segment": segment,
            "target_opened": target_opened,
        }
    )

    return data


def main():
    params = load_params()

    n_samples = params["dataset"]["n_samples"]
    random_state = params["dataset"]["random_state"]

    output_path = Path("data/raw/openrate_mock.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    data = generate_dataset(n_samples, random_state)
    data.to_csv(output_path, index=False)

    print("Dataset mock creado correctamente.")
    print(f"Ruta: {output_path}")
    print(f"Filas: {data.shape[0]}")
    print(f"Columnas: {data.shape[1]}")


if __name__ == "__main__":
    main()