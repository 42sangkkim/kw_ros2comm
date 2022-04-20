import rclpy
import ros2client.comm as comm

def main(args=None):
	rclpy.init(args=args)
	print("Client Run!")
	client_publisher = comm.ClientPublisher()

	rclpy.spin(client_publisher)

	client_publisher.destroy_node()
	rclpy.shutdown

if __name__ == '__main__':
    main()
