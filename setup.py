from setuptools import setup

package_name = 'rlb_sim_clock'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vguillet',
    maintainer_email='victor.guillet@protonmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rlb_sim_clock = rlb_sim_clock.rlb_sim_clock:main'
        ],
    },
)
