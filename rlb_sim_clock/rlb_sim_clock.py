
from datetime import datetime
import rclpy
from rclpy.node import Node
from rlb_utils.msg import TeamComm
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy


class rlb_sim_clock(Node):
    def __init__(self):
        super().__init__('rlb_clock')
        self.start_time = datetime.now()

        qos = QoSProfile(
            reliability=QoSReliabilityPolicy.RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT,
            history=QoSHistoryPolicy.RMW_QOS_POLICY_HISTORY_KEEP_LAST,
            depth=1
            )

        self.clock_publisher = self.create_publisher(
            msg_type=TeamComm,
            topic="/RLB_clock",
            qos_profile=qos
            )

        while True:
            self.publish_timestamp()
            
            print(self.sim_time)

        # self.timer = self.create_timer(
        #     timer_period_sec=0.001,
        #     callback=self.publish_timestamp
        # )

        # self.print_timer = self.create_timer(
        #     timer_period_sec=1.0,
        #     callback=self.print_time
        # )
    
    @property
    def sim_time(self):
        return datetime.now() - self.start_time

    def print_time(self):
        print(self.sim_time)

    def publish_timestamp(self):
        msg = TeamComm()
        msg.source = "clock"
        msg.source_type = "clock"
        msg.type = "clock"
        msg.data = str(self.sim_time.total_seconds())

        self.clock_publisher.publish(msg=msg)


def main(args=None):
    # `rclpy` library is initialized
    rclpy.init(args=args)

    path_sequence = rlb_sim_clock()

    rclpy.spin(path_sequence)

    path_sequence.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
