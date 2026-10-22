class ReactorExpertSystem:
    def __init__(self, temperature, pressure, coolant_flow, radiation_level):
        self.temp = temperature
        self.press = pressure
        self.flow = coolant_flow
        self.rad = radiation_level

    def _fuzzify_temperature(self):
        if self.temp <= 300:
            return {"Normal": 1.0, "High": 0.0, "Critical": 0.0}
        elif 300 < self.temp <= 500:
            high_membership = (self.temp - 300) / 200
            return {"Normal": 1.0 - high_membership, "High": high_membership, "Critical": 0.0}
        elif 500 < self.temp <= 650:
            critical_membership = (self.temp - 500) / 150
            return {"Normal": 0.0, "High": 1.0 - critical_membership, "Critical": critical_membership}
        else:
            return {"Normal": 0.0, "High": 0.0, "Critical": 1.0}

    def diagnose_event_tree(self):
        is_low_pressure = self.press < 7.0
        is_low_flow = self.flow < 45
        is_high_rad = self.rad > 100

        if is_low_pressure and is_low_flow and is_high_rad:
            return "DIAGNOSIS: Major Loss-of-Coolant Accident (LOCA) with Fuel Core Degradation."
        elif is_low_pressure and is_low_flow:
            return "DIAGNOSIS: Potential Pipe Rupture / Minor LOCA detected."
        elif is_low_flow and self.temp > 550:
            return "DIAGNOSIS: Flow-to-Power Mismatch (Anticipated Transient Without Scram risk)."
        return "DIAGNOSIS: No specific accident fingerprint matched. Proceeding to function monitoring."

    def evaluate_system(self):
        print("--- Telemetry Inputs ---")
        print(f"Temp: {self.temp}°C | Pressure: {self.press} MPa | Flow: {self.flow}% | Rad: {self.rad} mSv/h\n")

        event_diagnosis = self.diagnose_event_tree()
        print(event_diagnosis)
        print("-" * 50)

        temp_zones = self._fuzzify_temperature()
        print(f"Fuzzy Temperature Breakdown -> High Risk: {temp_zones['High']:.2f} | Critical Risk: {temp_zones['Critical']:.2f}")

        actions = []

        if temp_zones["Critical"] > 0.3:
            actions.append(f"[EMERGENCY] Automated SCRAM required. Confidence: {temp_zones['Critical']:.2f}")
        elif temp_zones["High"] > 0.5:
            actions.append(f"[ACTION] Deploy auxiliary cooling system loops. Confidence: {temp_zones['High']:.2f}")

        if self.flow < 30:
            actions.append("[EMERGENCY] Emergency Core Cooling System (ECCS) actuation required immediately.")

        if not actions and "LOCA" not in event_diagnosis:
            actions.append("[STATUS] All critical safety functions operating within baseline parameters.")

        print("\nRecommended Emergency Treatments:")
        for action in actions:
            print(f" -> {action}")

if __name__ == "__main__":
    simulated_reactor = ReactorExpertSystem(
        temperature=580,
        pressure=5.2,
        coolant_flow=25,
        radiation_level=120
    )

    simulated_reactor.evaluate_system()
