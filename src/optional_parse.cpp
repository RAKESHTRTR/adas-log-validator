#include <iostream>
#include <optional>
#include <string>
#include <vector>

std::optional<double> parse_sensor_val(const std::string& raw) {
    if (raw.empty() || raw == "NaN" || raw == "ERR") {
        return std::nullopt;
    }
    try {
        size_t idx = 0;
        double val = std::stod(raw, &idx);
        if (idx != raw.size()) return std::nullopt; // Reject trailing garbage like "15.4abc"
        return val;
    } catch (...) {
        return std::nullopt;
    }
}

int main() {
    std::vector<std::string> samples = {"15.4", "NaN", "ERR", "22.1", "12.0xyz", ""};
    for (const auto& s : samples) {
        auto v = parse_sensor_val(s);
        if (v.has_value()) {
            std::cout << "'" << s << "' -> OK: " << *v << "\n";
        } else {
            std::cout << "'" << s << "' -> MISSING/CORRUPTED (skipped)\n";
        }
    }
    return 0;
}