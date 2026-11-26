#include <atomic>
#include <condition_variable>
#include <iostream>
#include <mutex>
#include <queue>
#include <thread>

std::mutex mtx;
std::condition_variable cv;
std::queue<int> frame_queue;
std::atomic<bool> done{false};

void sensor_producer() {
    for (int frame_id = 1; frame_id <= 10; ++frame_id) {
        {
            std::lock_guard<std::mutex> lock(mtx);
            frame_queue.push(frame_id * 100); // Simulated timestamp_ms
        }
        cv.notify_one();
    }
    done = true;
    cv.notify_all();
}

void disk_consumer() {
    while (true) {
        std::unique_lock<std::mutex> lock(mtx);
        cv.wait(lock, [] { return !frame_queue.empty() || done.load(); });
        while (!frame_queue.empty()) {
            std::cout << "Logged frame ts=" << frame_queue.front() << "ms\n";
            frame_queue.pop();
        }
        if (done.load()) break;
    }
}

int main() {
    std::thread t_prod(sensor_producer);
    std::thread t_cons(disk_consumer);
    t_prod.join();
    t_cons.join();
    return 0;
}
