import rclpy
import os
from rclpy.node import Node
from wallter_interfaces.msg import AkkuStats 
from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            AkkuStats,
            'topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        os.system('cls||clear')


    def listener_callback(self, msg):
        os.system('cls||clear')
        print('Bus: ' + format(msg.bus_voltage, '.2f') + 'V')
        print('Load: ' + format(msg.load_voltage, '.2f') + 'V')
        print('Shunt: ' + format(msg.shunt_voltage, '.2f') + 'mV')
        print('Current: ' + format(msg.current, '.2f') + 'mA')
        print('Power: ' + format(msg.power) + 'mW')
        #self.get_logger().info('Bus: "%f"' % msg.bus_voltage)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()