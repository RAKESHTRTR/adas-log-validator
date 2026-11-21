#include <iostream>
#include <memory>

struct SensorFrame {
    int id;
    double ttc_s;
    ~SensorFrame() { std::cout << "Freed frame " << id << "\n"; }
};

int main() {
    auto f = std::make_unique<SensorFrame>(SensorFrame{101, 1.85});
    std::cout << "Processing frame " << f->id << " TTC=" << f->ttc_s << "\n";
    return 0; // Automatically freed here (RAII)
}
