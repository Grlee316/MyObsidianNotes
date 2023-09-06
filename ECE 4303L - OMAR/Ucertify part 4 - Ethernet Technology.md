
Odds are, when you are working with local area networks (LANs), you are working with Ethernet as the Layer 1 technology. Back in the mid-1990s, there was tremendous competition between technologies such as Ethernet, Token Ring, and Fiber Distributed Data Interface (FDDI). Today, however, you can see that Ethernet is the clear winner of those Layer 1 wars.  
  
Of course, over the years, Ethernet has evolved. Several Ethernet standards exist in modern LANs, with a variety of distance and speed limitations. This lesson begins by reviewing the fundamentals of Ethernet networks, including a collection of Ethernet speeds and feeds.  
  
Lesson 3, "Network Components," introduced you to Ethernet switches. Because these switches are such an integral part of LANs, this lesson delves into many of the features offered by some Ethernet switches.

# 4.1 Principles of Ethernet

The genesis of Ethernet was 1973, when this technology was developed by Xerox Corporation. The original intent was to create a technology to allow computers to connect with laser printers. A quick survey of many corporate network reveals that Ethernet rose well beyond its humble beginnings, with Ethernet being used to interconnect such devices as computers, printers, wireless access points, servers, switches, routers, video-game systems, and more. This section discusses early Ethernet implementations and limitations and references up-to-date Ethernet throughput and distance specifications.

#### Ethernet Origins

In the network-industry literature, you might come upon the term _IEEE 802.3_ (where IEEE refers to the Institute of Electrical and Electronics Engineers standards body). In general, you can use the term _IEEE 802.3_ interchangeably with the term _Ethernet_. However, be aware that these technologies have some subtle distinctions. For example, an Ethernet frame is a fixed-length frame, whereas an 802.3 frame length can vary.  
  
A popular implementation of Ethernet, in the early days, was called _10BASE5_. The 10 in 10BASE5 referred to network throughput, specifically 10Mbps (that is, 10 million [mega] bits per second). The BASE in 10BASE5 referred to baseband, as opposed to broadband, as discussed in Lesson 2, "The OSI Reference Model." Finally, the 5 in 10BASE5 indicated the distance limitation of 500 meters. The cable used in 10BASE5 networks, as shown in Figure 4-1, was a larger diameter than most types of media. In fact, this network type became known as _thicknet_.  
  

![The figure shows a 10BASE5 coaxial cable.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig01.jpg)

Figure 4-1: 10BASE5 Cable

  
Another early Ethernet implementation was 10BASE2. From the previous analysis of 10BASE5, you might conclude that 10BASE2 was a 10Mbps baseband technology with a distance limitation of 200 meters. That is almost correct. However, 10BASE2's actual distance limitation was 185 meters. The cabling used in 10BASE2 networks was significantly thinner and therefore less expensive than 10BASE5 cabling. As a result, 10BASE2 cabling, as shown in Figure 4-2, was known as _thinnet_ or _cheapernet_.  
  

![The figure shows a 10BASE2 coaxial cable.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig02.jpg)

Figure 4-2: Coaxial Cable Used for 10BASE2

  
10BASE5 and 10BASE2 networks are rarely, if ever, seen today. Other than their 10Mbps bandwidth limitation, the cabling used by these legacy technologies quickly faded in popularity with the advent of unshielded twisted-pair (UTP) cabling, as discussed in Lesson 2. The 10Mbps version of Ethernet that relied on UTP cabling, an example of which is provided in Figure 4-3, is known as _10BASE-T_, where the T in 10BASE-T refers to twisted-pair cabling.  
  

![The figure shows a 10BASE-T UTP cable.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig03.jpg)

Figure 4-3: UTP Cable Used for 10BASE-T

#### Carrier-Sense Multiple Access/Collision Detect

Ethernet was based on the philosophy that all networked devices should be eligible, at any time, to transmit on a network. This school of thought is in direct opposition to technologies such as Token Ring, which boasted a _deterministic_ media access approach. Specifically, Token Ring networks passed a token around a network in a circular fashion, from one networked device to the next. Only when a networked device was in possession of that token was it eligible to send on the network.  
  
Recall from Lesson 1, "Computer Network Fundamentals," the concept of a bus topology. An example of a bus topology is a long cable (such as thicknet or thinnet) running the length of a building, with various networked devices tapping into that cable to gain access to the network.  
Consider Figure 4-4, which depicts an Ethernet network using a shared bus topology.  
  

![A figure illustrates the usage of a shared bus topology by an Ethernet network. The figure shows an Ethernet bus connected to six devices: two Pcs and a file server at the top, and three PCs at the bottom.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig04.jpg)

Figure 4-4: Ethernet Network Using a Shared Bus Topology

  
In this topology, all devices are directly connected to the network and are free to transmit at any time, if they have reason to believe no other transmission currently exists on the wire. Ethernet permits only a single frame to be on a network segment at any one time. So, before a device in this network transmits, it listens to the wire to see if there is currently any traffic being transmitted. If no traffic is detected, the networked device transmits its data. However, what if two devices simultaneously had data to send? If they both listen to the wire at the same time, they could simultaneously, and erroneously, conclude that it is safe to send their data. However, when both devices simultaneously send their data, a _collision_ occurs. A collision, as depicted in Figure 4-5, results in data corruption.  
  

![A figure depicts the data corruption on an Ethernet network. The figure shows an Ethernet bus connected to six devices: three PCs at the top and three PCs at the bottom. Arrows from the first and second PC at the bottom points to a starburst that has red dots on either side in the Ethernet segment.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig05.jpg)

Figure 4-5: Collision on an Ethernet Segment

  
Fortunately, Ethernet was designed with a mechanism to detect collisions and allow the devices whose transmissions collided to retransmit their data at different times. Specifically, after the devices notice that a collision occurred, they independently set a random _back-off timer_. Each device waits for this random amount of time to elapse before again trying to transmit. Here is the logic: Because each device certainly picked a different amount of time to back off from transmitting, their transmissions should not collide the next time these devices transmit, as illustrated in Figure 4-6.  
  

![A figure depicts recovering from a data corruption by using random back-off timers. The figure shows an Ethernet bus connected to six devices: three PCs at the top and three PCs at the bottom. The first PC at the bottom has a random back-off timer of 100 ms. The second PC at the bottom has a random back-off timer of 200 ms.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig06.jpg)

Figure 4-6: Recovering from a Collision with Random Back-off Timers

  
The procedure used by Ethernet to decide whether it is safe to transmit, detect collisions, and retransmit if necessary is called _carrier-sense multiple access/collision detection_ (CSMA/CD).  
  
Let's break down CSMA/CD into its constituent components:  

- **Carrier sense:** A device attached to an Ethernet network can listen to the wire, prior to transmitting, to make sure that a frame is not being transmitted on the network segment.
- **Multiple access:** Unlike a deterministic method of network access (for example, the method used by Token Ring), all Ethernet devices simultaneously have access to an Ethernet segment.
- **Collision detection:** If a collision occurs (perhaps because two devices were simultaneously listening to the network and simultaneously concluded that it was safe to send), Ethernet devices can detect that collision and set random back-off timers. After each device's random timer expires, it again tries to transmit its data.

Even with Ethernet's CSMA/CD feature, Ethernet segments still suffer from scalability limitations. Specifically, the likelihood of collisions increases as the number of devices on a shared Ethernet segment increases.  
  
An alternate approach is CSMA/CA. Here, CA refers to using _collision avoidance_. This technology is common in wireless networks and was made famous by Token Ring in early LANs.  
  
Regarding wired Ethernet, devices on a shared Ethernet segment belong to the same _collision domain_. One example of a shared Ethernet segment is a 10BASE5 or 10BASE2 network with multiple devices attaching to the same cable. On that cable, only one device can send at any one time. Therefore, all devices attached to the thicknet or thinnet cable are in the same collision domain.  
  
Similarly, devices connected to an Ethernet hub are, as shown in Figure 4-7, in the same collision domain. As described in Lesson 3, a hub is a Layer 1 device and does not make forwarding decisions. Instead, a hub takes bits in on one port and sends them out all the other hub ports except the one on which the bits were received.  
  

![A figure shows an Ethernet hub at the center that is connected to four devices. Three PCs: one at the top, one on the right, and one at the bottom, and a printer at the bottom-right. Text at the bottom reads "one collision domain".](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig07.jpg)

Figure 4-7: Shared Ethernet Hub: One Collision Domain

  
Ethernet switches, as in Figure 4-8, dramatically increase the scalability of Ethernet networks by creating multiple collision domains. In fact, every port on an Ethernet switch is in its own collision domain.  
  

![A figure shows a layer 2 switch at the center connected to four devices: a PC at the top and bottom, a file server on the left, and a printer at the bottom-right. Text at the bottom reads "four collision domains".](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig08.jpg)

Figure 4-8: Ethernet Switch: One Collision Domain per Port

  
A less-obvious but powerful benefit also goes with Ethernet switches. Because a switch port is connecting to a single device, there is no chance of having a collision. With no chance of collision, collision detection is no longer needed. With collision detection disabled, network devices can run in _full-duplex_ mode rather than _half-duplex_ mode. In full-duplex mode, a device can simultaneously send and receive at the same time.  
  
When multiple devices are connected to the same shared Ethernet segment such as a Layer 1 hub, CSMA/CD must be enabled. As a result, the network must work in half-duplex mode, which means that only a single networked device can transmit or receive at any one time. In half-duplex mode, a networked device cannot simultaneously send and receive, which is an inefficient use of a network's bandwidth.

#### Distance and Speed Limitations

To understand the bandwidth available on networks, you need to define a few terms. You should already know that a _bit_ refers to one of two values. These values are represented using binary math, which uses only the numbers 0 and 1. On a cable such as twisted-pair cable, a bit could be represented by the absence or presence of voltage. Fiber-optic cables, however, might represent a bit with the absence or presence of light.  
  
The bandwidth of a network is measured in terms of how many bits the network can transmit during a 1-second period of time. For example, if a network has the capacity to send 10,000,000 (that is, 10 million) bits in a 1-second period of time, the bandwidth capacity is said to be 10 megabits (that is, millions of bits) per second (or _Mbps_). Table 4-1 defines common bandwidths supported on distinct types of Ethernet networks.

![[Pasted image 20230716162859.png]]

The type of cabling used in your Ethernet network influences the bandwidth capacity and the distance limitation of your network. For example, fiber-optic cabling often has a higher bandwidth capacity and a longer distance limitation than twisted-pair cabling.  
  
Recall from Lesson 3 the contrast of single-mode fiber (SMF) to multimode fiber (MMF). Because of the issue of multimode delay distortion, SMF usually has a longer distance limitation than MMF.  
  
When you want to uplink one Ethernet switch to another, you might need different connectors (for example, MMF, SMF, or UTP) for different installations. Fortunately, some Ethernet switches have one or more empty slots in which you can insert a gigabit interface converter (GBIC). GBICs are interfaces that have a bandwidth capacity of 1Gbps and are available with MMF, SMF, and UTP connectors. This allows you to have flexibility in the uplink technology you use in an Ethernet switch.  
  
The various interface converters are commonly called transceivers. Two common characteristics of fiber optic transceivers are that they are bidirectional and (full) duplex. This means they can send data in both directions (bidirectional), and that they can do so simultaneously (full duplex).

**Note**
A smaller variant of a regular GBIC is the small form-factor pluggable (SFP), which is sometimes called a _mini-GBIC_. Variations of the SFP include SFP+ and QSFP.

![[Pasted image 20230716163022.png]]
![[Pasted image 20230716163044.png]]

**Note**

Two often-confused terms are _100BASE-T_ and _100BASE-TX_. 100BASE-T itself is not a specific standard. Rather, 100BASE-T is a category of standards and includes 100BASE-T2 (which uses two pairs of wires in a Cat 3 cable), 100BASE-T4 (which uses four pairs of wires in a Cat 3 cable), and 100BASE-TX. 100BASE-T2 and 100BASE-T4 were early implementations of 100Mbps Ethernet and are no longer used. Therefore, you can generally use the terms _100BASE-T_ and _100BASE-TX_ interchangeably.  
  
Similarly, the term _1000BASE-X_ is not a specific standard. Rather, 1000BASE-X refers to all Ethernet technologies that transmit data at a rate of 1Gbps over fiber-optic cabling. Additional and creative ways of using Ethernet technology include IEEE 1901-2013, which could be used for Ethernet over HDMI cables and Ethernet over existing power lines to avoid having to run a separate cabling just for networking.


## IMPORTANT
The IEEE 802.3 standard is also known as **Ethernet**. 10BASE5 was a popular implementation of Ethernet and was also termed **thicknet**. 10BASE2 was also an earlier implementation of Ethernet. The network throughput or bandwidth capacity of both 10BASE5 and 10BASE2 was 10 Mbps, while they have distance limitations of **500** meters and **185** meters, respectively.

The following are correct statements about network data transmission in an Ethernet network:

- A collision occurs on an Ethernet segment when two devices simultaneously send their data.
- After the devices notice that a collision has occurred, they independently set a random back-off-timer.
- Carrier Sense Multiple Access with Collision Detection (CSMA/CD) is a procedure used by Ethernet to decide whether it is safe to transmit, detect collisions, and retransmit if necessary. CSMA/CA is used to avoid collision.
- Devices connected to an Ethernet hub belong to the same collision domain.
- With an Ethernet, there is no chance of collision because each device belongs to a separate collision domain.


# 4.2 Ethernet Switch Features
Lesson 3 delved into the operation of Layer 2 Ethernet switches (which we generically refer to as _switches_). You read an explanation of how a switch learns which Media Access Control (MAC) addresses live off of which ports and an explanation of how a switch makes forwarding decisions based on destination MAC addresses.  
  
Beyond basic frame forwarding, however, many Layer 2 Ethernet switches offer a variety of other features to enhance such things as network performance, redundancy, security, management, flexibility, and scalability. Although the specific features offered by a switch vary, this section introduces you to some of the more common features found on switches.

#### Virtual LANs

In a basic switch configuration, all ports on a switch belong to the same _broadcast domain_, as explained in Lesson 3. In such an arrangement, a broadcast received on one port gets forwarded out to all other ports.  
  
Also, from a Layer 3 perspective, all devices connected in a broadcast domain have the same _network address_. Lesson 5, "IPv4 and IPv6 Addresses," gets into the binary math behind the scenes of how networked devices can be assigned an IP address (that is, a logical Layer 3 address). A portion of that address is the address of the network to which that device is attached. The remaining portion of that address is the address of the device itself. Devices that have the same network address belong to the same network or _subnet_.  
  
Imagine that you decide to place PCs from different departments within a company into their own subnet. One reason you might want to do this is for security purposes. For example, by having the Accounting department in a separate subnet (that is, a separate broadcast domain) than the Sales department, devices in one subnet will not see the broadcasts being sent on the other subnet.  
  
A design challenge might be that PCs belonging to these departments are scattered across multiple floors in a building. Consider Figure 4-9 as an example. The Accounting and Sales departments each have a PC on both floors of a building. Because the wiring for each floor runs back to a wiring closet on that floor, to support these two subnets using a switch's default configuration, you would have to install two switches on each floor. For traffic to travel from one subnet to another subnet, that traffic has to be routed, meaning that a device such as a multilayer switch or a router forwards traffic based on a packet's destination network addresses. So, in this example, the Accounting switches are interconnected and then connect to a router, and the Sales switches are connected similarly.  
  

![A figure shows the ports of a switch belonging to the same subnet. The figure shows four switches: two at the top and two at the bottom. A switch at the top is connected to a switch at the bottom. Next, to it, two sections: Account and sales, are shown. Each section has two PCs: one at the top and one at the bottom. The top portion is labeled "floor 2" and the bottom portion is labeled "floor 1." A Switch at the top is connected to a PC on the account section. Another PC is connected to the PC at the sales section. A switch at the bottom is connected to the PC of the account section. Another switch is connected to the PC of the sales section. The two switches at the bottom are connected to a router.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig09.jpg)

Figure 4-9: Example: All Ports on a Switch Belonging to the Same Subnet

  
The design presented lacks efficiency, in that you have to install at least one switch per subnet. A more efficient design would be to logically separate a switch's ports into different broadcast domains. Then, in the example, an Accounting department PC and a Sales department PC could connect to the same switch, even though those PCs belong to different subnets. Fortunately, _virtual LANs_ (VLANs) make this possible.  
  
With VLANs, as illustrated in Figure 4-10, a switch can have its ports logically divided into more than one broadcast domain (that is, more than one subnet or VLAN). Then, devices that need to connect to those VLANs can connect to the same physical switch, yet logically be separate from one another.  
  

![A figure shows the ports of a switch belonging to different VLANs. The figure shows two switches: one at the top and one at the bottom. Next, to it, two sections: Account and sales, are shown. Each section has two PCs: one at the top and one at the bottom. The top portion is labeled "floor 2" and the bottom portion is labeled "floor 1." The switch at the top is connected to the PCs at the top of the sections. The switch at the bottom is connected to the PCs at the bottom of the sections. The switches are connected via a 2-wire circuit. The switch at the bottom is connected to a router via a 2-wire circuit.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig10.jpg)

Figure 4-10: Example: Ports on a Switch Belonging to Different VLANs

  
One challenge with VLAN configuration in large environments is the need to configure identical VLAN information on all switches. Manually performing this configuration is time-consuming and error-prone. However, switches from Cisco Systems support VLAN Trunking Protocol (VTP), which allows a VLAN created on one switch to be propagated to other switches in a group of switches (that is, a VTP domain). VTP information is carried over a _trunk connection_, which is discussed next.

#### Switch Configuration for an Access Port

Configurations used on a switch port may vary, based on the manufacturer of the switch. Example 4-1 shows a sample configuration on an access port (no trunking) on a Cisco Catalyst switch. Lines with a leading ! are being used to document the next line(s) of the configuration.  
  
**Example 4-1** Switch Access Port Configuration
```
! Move into configuration mode for interface gig 0/21  
SW1(config)# **interface GigabitEthernet0/21**  
  
! Add a text description of what the port is used for  
SW1(config-if)# **description Access port in Sales VLAN 21**  
  
! Define the port as an access port, and not a trunk port  
SW1(config-if)# **switchport mode access**  
  
! Assign the port to VLAN 21  
SW1(config-if)# **switchport access vlan 21**  
  
! Enable port security  
SW1(config-if)# **switchport port-security**  
  
! Control the number of MAC addresses the switch may learn  
! from device(s) connected to this switch port  
SW1(config-if)# **switchport port-security maximum 5**  
  
! Restrict any frames from MAC addresses above the 5 allowed  
SW1(config-if)# **switchport port-security violation restrict**  
  
! Set the speed to 1,000 Mbps (1 Gigabit per second)  
SW1(config-if)# **speed 1000**  
  
! Set the duplex to full  
SW1(config-if)# **duplex full**  
  
! Configure the port to begin forwarding without waiting the  
! standard amount of time normally set by Spanning Tree Protocol  
SW1(config-if)# **spanning-tree portfast**
```

#### Trunks

One challenge with carving a switch up into multiple VLANs is that several switch ports (that is, one port per VLAN) could be consumed connecting a switch to a switch, or a switch to a router. A more efficient approach is to allow traffic for multiple VLANs to travel over a single connection, as shown in Figure 4-11. This type of connection is called a _trunk_.  
  

![A figure depicts the trunking between switches. The figure shows two switches: one at the top and one at the bottom. Next, to it, two sections: Account and sales, are shown. Each section has two PCs: one at the top and one at the bottom. The top portion is labeled "floor 2" and the bottom portion is labeled "floor 1." The switch at the top is connected to the PCs at the top of the sections. The switch at the bottom is connected to the PCs at the bottom of the sections. The switches are connected via a 2-wire trunk connection. The switch at the bottom is connected to a router via a trunk connection.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig11.jpg)

Figure 4-11: Example: Trunking Between Switches

  
The most popular trunking standard today is IEEE 802.1Q, which is often referred to as _dot1q_. One of the VLANs traveling over an 802.1Q trunk is called a _native VLAN_. Frames belonging to the native VLAN are sent unaltered over the trunk (untagged/no tag). However, to distinguish other VLANs from one another, the remaining VLANs are tagged.  
  
Specifically, a nonnative VLAN has four tag bytes (where a _byte_ is a collection of 8 bits) added to the Ethernet frame (tagged frame). Figure 4-12 shows the format of an IEEE 802.1Q header with these 4 bytes.  
  

![Header format of IEEE 802.1Q shows a layer divided into nine fields. The field headers read, preamble 7 bytes, start-of-frame delimiter 1 byte, destination address 6 bytes, source address 6 bytes, tag protocol identifier 2 bytes, tag control identifier 2 bytes, type 2 bytes, data, and CRC/FCS 4 bytes. The fields tag protocol identifier 2 bytes and tag control identifier 2 bytes are collectively labeled 4 bytes added by IEEE 802.1Q.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig12.jpg)

Figure 4-12: IEEE 802.1Q Header

  
One of these bytes contains a VLAN field. That field indicates to which VLAN a frame belongs. The devices (for example, a switch, a multilayer switch, or a router) at each end of a trunk interrogate that field to determine to which VLAN an incoming frame is associated. As you can see by comparing Figures 4-9, 4-10, and 4-11, VLAN and trunking features allow switch ports to be used far more efficiently than merely relying on a default switch configuration.

#### Switch Configuration for a Trunk Port

Example 4-2 shows a sample configuration on a trunk port on a Cisco Catalyst switch. Again, lines with a leading ! are being used to document the next line(s) of the configuration.  
  
**Example 4-2** Sample Trunk Port Configuration
```
! Go to interface config mode for interface Gig 0/22  
SW1(config)# **interface GigabitEthernet0/22**  
  
! Add a text description  
SW1(config-if)# **description Trunk to another switch**  
  
! Specify that this is a trunk port  
SW1(config-if)# **switchport mode trunk**  
  
! Specify the trunking protocol to use  
SW1(config-if)# **switchport trunk encapsulation dot1q**  
  
! Specify the native VLAN to use for un-tagged frames  
SW1(config-if)# **switchport trunk native vlan 5**  
  
! Specify which VLANs are allowed to go on the trunk  
SW1(config-if)# **switchport trunk allowed vlan 1-50**
```

#### Spanning Tree Protocol

Administrators of corporate telephone networks often boast about their telephone system—that is, a private branch exchange (PBX) system—having the _five nines_ of availability. If a system has five nines of availability, it is up and functioning 99.999 percent of the time, which translates to only about 5 minutes of downtime per year.  
  
Traditionally, corporate data networks struggled to compete with corporate voice networks, in terms of availability. Today, however, many networks that traditionally carried only data now carry voice, video, and data. Therefore, availability becomes an even more important design consideration.  
  
To improve network availability at Layer 2, many networks have redundant links between switches. However, unlike Layer 3 packets, Layer 2 frames lack a Time-to-Live (TTL) field. As a result, a Layer 2 frame can circulate endlessly through a looped Layer 2 topology. Fortunately, IEEE 802.1D Spanning Tree Protocol (STP) allows a network to physically have Layer 2 loops while strategically blocking data from flowing over one or more switch ports to prevent the looping of traffic.  
  
In the absence of STP, if we have parallel paths, two significant symptoms include corruption of a switch's MAC address table and broadcast storms, where frames loop over and over throughout our switched network. An enhancement to the original STP protocol is _802.1w_, which is also called _Rapid Spanning Tree_ because it does a quicker job of adjusting to network conditions, such as the addition to or removal of Layer 2 links in the network.  
  
Shortest Path Bridging (IEEE 802.1aq/SPB) is a protocol that is more scalable in larger environments (hundreds of switches interconnected) compared to STP.

#### Corruption of a Switch's MAC Address Table

As described in Lesson 3, a switch's MAC address table can dynamically learn what MAC addresses are available off its ports. However, in the case of an STP failure, a switch's MAC address table can become corrupted. To illustrate, consider Figure 4-13.  
  

![A figure shows the corruption of a MAC Address table. The figure shows two switches, SW1 and SW2 on the left and right, respectively. The ports Gig 0/1 of SW1 and Gig 0/1 of SW2 are connected to a segment A at the top and the ports Gig 0/2 of SW1 and Gig 0/2 of Sw2 are connected to a segment B at the bottom. PC1 with MAC Address AAAA.AAAA.AAAA is connected to the segment A at the top-right corner. PC2 is connected to segment B at the bottom-left corner. An arrow from PC1 goes to SW1 and SW2. An arrow from SW2 goes to PC2. A double-headed arrow is shown between PC2 and SW2. A table titled "Switch A's MAC Address table" shows two columns and two rows. The column headers read, port and MAC Addresses. Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA (block icon is shown in the cell). Row 2 reads, Gig 0/2 and AAAA.AAAA.AAAA. . A table titled "Switch B's MAC Address table" shows two columns and two rows. The column headers read, port and MAC Addresses. Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA (block icon is shown in the cell). Row 2 reads, Gig 0/2 and AAAA.AAAA.AAAA.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig13.jpg)

Figure 4-13: MAC Address Table Corruption

  
PC1 is transmitting traffic to PC2. When the frame sent from PC1 is transmitted on segment A, the frame is seen on the Gig 0/1 ports of switches SW1 and SW2, causing both switches to add an entry to their MAC address tables associating a MAC address of AAAA.AAAA.AAAA with port Gig 0/1. Because STP is not functioning, both switches then forward the frame out on segment B. As a result, PC2 receives two copies of the frame. Also, switch SW1 sees the frame forwarded out of switch SW2's Gig 0/2 port. Because the frame has a source MAC address of AAAA.AAAA.AAAA, switch SW1 incorrectly updates its MAC address table, indicating that a MAC address of AAAA.AAAA.AAAA resides off of port Gig 0/2. Similarly, switch SW2 sees the frame forwarded on to segment B by switch SW1 on its Gig 0/2 port. Therefore, switch SW2 also incorrectly updates its MAC address table.

#### Broadcast Storms

As previously mentioned, when a switch receives a broadcast frame (that is, a frame destined for a MAC address of FFFF.FFFF.FFFF), the switch floods the frame out of all switch ports, other than the port on which the frame was received. Because a Layer 2 frame does not have a TTL field, a broadcast frame endlessly circulates through the Layer 2 topology, consuming resources on both switches and attached devices (for example, user PCs).  
  
Figure 4-14 and the following list illustrate how a broadcast storm can form in a Layer 2 topology when STP is not functioning correctly:  
  

![A figure illustrates the broadcast storm. The figure shows two switches, SW1 and SW2 on the left and right, respectively. The ports Gig 0/1 of SW1 and Gig 0/1 of SW2 are connected to a segment A at the top and the ports Gig 0/2 of SW1 and Gig 0/2 of Sw2 are connected to a segment B at the bottom. PC1 is connected to the segment A at the top-right corner. PC2 is connected to segment B at the bottom-left corner. An arrow labeled "broadcast frame destined for FFFF.FFFF.FFFF from PC1 goes to SW1 and SW2. An arrow from SW2 goes to PC2. A double-headed arrow is shown between PC2 and SW2. A double-headed arrow is shown between SW1 and PC1. A dashed arrow from SW1 goes to PC1 and SW2.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig14.jpg)

Figure 4-14: Broadcast Storm
1. PC1 sends a broadcast frame on to segment A, and the frame enters each switch on port Gig 0/1.
2. Both switches flood a copy of the broadcast frame out of their Gig 0/2 ports (that is, on to segment B), causing PC2 to receive two copies of the broadcast frame.
3. Both switches receive a copy of the broadcast frame on their Gig 0/2 ports (that is, from segment B) and flood the frame out of their Gig 0/1 ports (that is, on to segment A), causing PC1 to receive two copies of the broadcast frame.

This behavior continues as the broadcast frame copies continue to loop through the network. The performance of PC1 and PC2 is affected because they also continue to receive copies of the broadcast frame.

#### STP Operation

STP prevents Layer 2 loops from occurring in a network because such an occurrence might result in a broadcast storm or corruption of a switch's MAC address table. Switches in an STP topology are classified as one of the following:  

- **Root bridge:** A switch elected to act as a reference point for a spanning tree. The switch with the lowest bridge ID (BID) is elected as the root bridge. The BID is made up of a priority value and a MAC address.
- **Nonroot bridge:** All other switches in the STP topology are nonroot bridges.

Figure 4-15 illustrates the root bridge election in a network. Notice that because the bridge priorities are both 32768, the switch with the lowest MAC address (that is, SW1) is elected as the root bridge.  
  

![A figure depicts the root bridge election. The figure shows two switches labeled SW1 (root bridge) and SW2 (non-root bridge). SW1 and SW2 are connected to a network segment 2 (fast Ethernet) at the bottom. SW1 is connected to a network segment 1 (fast Ethernet) with MAC Address: AAAA.AAAA.AAAA and priority: 32768 at the top. SW2 is connected to a network segment 1 (fast Ethernet) with MAC Address: BBBB.BBBB.BBBB and priority: 32768 at the top.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig15.jpg)

Figure 4-15: Root Bridge Election

  
Ports that interconnect switches in an STP topology are categorized as one of the port types described in Table 4-3

![[Pasted image 20230716164334.png]]
  
Figure 4-16 illustrates these port types. Notice the root port for switch SW2 is selected based on the lowest port ID because the costs of both links are equal. Specifically, each link has a cost of 19, because both links are Fast Ethernet links.  
  

![A figure illustrates the roles of STP ports. The figure shows two switches labeled "root bridge" and "non root bridge" on the left and right, respectively. The designated port of root bridge and non designated port of non root bridge are connected to a network segment 2 (fast Ethernet: cost =19) at the bottom. The designated port of root bridge and root port of non root bridge are connected to a network segment 1 (fast Ethernet: cost =19) at the top.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig16.jpg)

Figure 4-16: Identifying STP Port Roles

Figure 4-17 shows a similar topology to Figure 4-16. In Figure 4-17, however, the top link is running at a speed of 10Mbps, whereas the bottom link is running at a speed of 100Mbps. Because switch SW2 seeks to get back to the root bridge (that is, switch SW1) with the least cost, port Gig 0/2 on switch SW2 is selected as the root port.  
  

![Figure depicts different port costs. The figure shows two switches SW1 and SW2, labeled "root bridge" and "non root bridge" on the left and right, respectively. The designated port Gig 0/2 of root bridge and root port Gig 0/2 of non root bridge are connected to a network segment 2 (fast Ethernet: cost =19) at the bottom. The designated port Gig 0/1 of root bridge and non designated port Gig 0/1 of non root bridge are connected to a network segment 1 (fast Ethernet: cost =19) at the top.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig17.jpg)

Figure 4-17: STP with Different Port Costs

Specifically, port Gig 0/1 has a cost of 100, and Gig 0/2 has a cost of 19. Table 4-4 shows the port costs for various link speeds

![[Pasted image 20230716164437.png]]

Nondesignated ports do not forward traffic during normal operation but do receive bridge protocol data units (BPDUs). Switches exchange STP information in the form of BPDUs. These contain useful information for STP elections, path cost calculation, link suppression, and loop detection. If a link in the topology goes down, the nondesignated port detects the link failure and determines whether it needs to transition to the forwarding state.  
  
If a nondesignated port needs to transition to the forwarding state, it does not do so immediately. Rather, it transitions through the following states:  

- **Blocking:** The port remains in the blocking state for 20 seconds by default. During this time, the nondesignated port evaluates BPDUs in an attempt to determine its role in the spanning tree.
- **Listening:** The port moves from the blocking state to the listening state and remains in this state for 15 seconds by default. During this time, the port sources BPDUs, which inform adjacent switches of the port's intent to forward data.
- **Learning:** The port moves from the listening state to the learning state and remains in this state for 15 seconds by default. During this time, the port begins to add entries to its MAC address table.
- **Forwarding:** The port moves from the learning state to the forwarding state and begins to forward frames.

## Notes
STP prevents Layer 2 loops from occurring in a network. Switches in an STP topology are classified as:  

- **Root bridge:** A switch elected to act as a reference point for a spanning tree. The switch with the lowest bridge ID (BID) is elected as the root bridge.
- **Nonroot bridge:** All other switches in the STP topology are nonroot bridges.

Ports that interconnect switches in an STP topology are classified as:  

- **Root port:** Every nonroot bridge has a single root port, which is the port on that switch that is closest to the root bridge in terms of cost.
- **Designated port:** Every network segment has a single designated port, which is the port on that segment that is closest to the root bridge in terms of cost. Therefore, all ports on a root bridge are designated ports.
- **Nondesignated port:** Nondesignated ports block traffic to create a loop-free topology.

#### Link Aggregation

If all ports on a switch are operating at the same speed (for example, 1Gbps), the most likely ports to experience congestion are ports connecting to another switch or router. For example, imagine a wiring closet switch connected (via Fast Ethernet ports) to multiple PCs. That wiring closet switch has an uplink to the main switch for a building. Because this uplink port aggregates multiple 100Mbps connections and the uplink port is also operating at 100Mbps, it can quickly become congested if multiple PCs are transmitting traffic that needs to be sent over that uplink, as shown in Figure 4-18.  
  

![Figure depicts uplink congestion. <BR>A switch at the center is connected to three PCs on the left via 100 Mbps and a switch on the right via 100 Mbps uplink. Arrows from the three PCs points to the switch at the center. A starburst at the top of the switch reads, congestion.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig18.jpg)

Figure 4-18: Uplink Congestion

  
To help alleviate congested links between switches, you can (on some switch models) logically combine multiple physical connections into a single logical connection, over which traffic can be sent. This feature, as illustrated in Figure 4-19, is called _link aggregation_.  
  

![Diagram of a Link Aggregation is shown. Two switches: SW1 and SW 2 are shown connected via four-wire circuits on either side from port Gig 0/1-4 and Gig 0/1- 4 respectively. A ring-like circle is shown at the center of the wires.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig19.jpg)

Figure 4-19: Link Aggregation

  
Although vendor-proprietary solutions for link aggregation have existed for some time, a couple of common issues existed with some solutions:  

- Each link in the logical bundle was a potential single point of failure.
- Each end of the logical bundle had to be manually configured.

In 2000, the IEEE ratified the 802.3ad standard for link aggregation. The IEEE 802.3ad standard supports Link Aggregation Control Protocol (LACP). Unlike some of the older vendor proprietary solutions, LACP supports automatic configuration and prevents an individual link from becoming a single point of failure. Specifically, with LACP, if a link fails, that link's traffic is forwarded over a different link. Groups of interfaces that make up an EtherChannel bundle are often referred to as a _link aggregation group_ (LAG). Cisco Systems implementation is referred to as _EtherChannel_, and the terms _LACP_ and _EtherChannel_ are both commonly used. An EtherChannel group could be configured to act as a Layer 2 access port, and only support a single VLAN, or it could be configured to act as a Layer 2 802.1Q trunk to support multiple VLANs of the LAG. LAGs could also be configured as a Layer 3 routed interface if the switch supports that feature. In the case of a Layer 3 Ether-Channel, an IP address would be applied to the logical interface that represents the LAG. Another term related to LACP and LAGs is _port bonding_, which also refers to the same concept of grouping multiple ports and using them as a single logical interface.

#### LACP Configuration

Example 4-3 shows a sample configuration of LACP on a Cisco switch. Comment lines are preceded by an exclamation mark (!).  
  
**Example 4-3** LACP Configuration  
  
```
! Move to interface that will be part of the LACP group  
SW1(config)# **interface GigabitEthernet0/16**  
  
! Assign this interface to the LACP group 1  
SW1(config-if)# **channel-group 1 mode active**  
  
! Move to the other interface(s) that will be part of  
! the same group  
SW1(config-if)# **interface GigabitEthernet0/17**  
SW1(config-if)# **channel-group 1 mode active**  
  
! Configure the group of interfaces as a logical group  
! Configuration here will also apply the individual  
! interfaces that are part of the group  
SW1(config-if)# **interface Port-channel 1**  
  
! Apply the configuration desired for the group  
! LACP groups can be access or trunk ports depending  
! on how the configuration of the logical port-channel interface  
! In this example the LAG will be acting as a trunk  
SW1(config-if)# **switchport mode trunk**  
SW1(config-if)# **switchport trunk encapsulation dot1q**
```


#### Power over Ethernet

Some switches not only transmit data over a connected UTP cable, but they use that cable to provide power to an attached device. For example, imagine that you want to mount a wireless access point (AP) on the ceiling. Although no electrical outlet is available near the AP's location, you can, as an example, run a Cat 5 UTP plenum cable above the drop ceiling and connect it to the AP. Some APs allow the switch at the other end of the UTP cable to provide power over the same wires that carry data. Examples of other devices that might benefit by receiving power from an Ethernet switch include security cameras and IP phones.  
  
The switch feature that gives power to attached devices is called _Power over Ethernet_ (PoE), and it is defined by the IEEE 802.3af standard. As shown in Figure 4-20, the PoE feature of a switch checks for 25k ohms (25,000 ohms) of resistance in the attached device. To check the resistance, the switch applies as much as 10V of direct current (DC) across specific pairs of wires (that is, pins 1 and 2 combine to form one side of the circuit, and pins 3 and 6 combine to form the other side of the circuit) connecting back to the attached device and checks to see how much current flows over those wires. For example, if the switch applied 10V DC across those wires and noticed 0.4 mA (milliamps) of current, the switch concludes the attached device had 25k ohms of resistance across those wires (based on the formula _E_ = _IR_, where _E_ represents voltage, _I_ represents current, and _R_ represents resistance). The switch could then apply power across those wires.  
  

![Diagram of a PoE is shown. A Switch with PoE Support on the left and an IP phone on the right are shown. Two connectors RJ-45 are shown between the switch and the phone. Two parallel lines at the top are shown connecting the pin 3 and 6 from the connector besides the switch to the connector next to the phone. Another two parallel lines at the bottom are shown connecting the pin 1 and 2 respectively. Text above the switch and the connector reads Switch applies 2.8 – 10 V DC to two pairs of leads to detect a 25 Kilo Ohm resistor in the attached device.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig20.jpg)

Figure 4-20: PoE

  
The next thing the switch must determine is how much power the attached device needs. The switch makes this determination by applying 15.5 V–20.5V DC (making sure that the current never exceeds 100 mA) to the attached device, for a brief period of time (less than one-tenth of a second). The amount of current flowing to the attached device tells the switch the _power class_ of the attached device. The switch then knows how much power should be made available on the port connecting to the device requiring power, and it begins supplying an appropriate amount of voltage (in the range 44V–57V) to the attached device.  
  
The IEEE 802.3af standard can supply a maximum of 15.4W (watts) of power. However, a more recent standard, IEEE 802.3at, offers as much as 32.4W of power, enabling PoE to support a wider range of devices.

#### Port Monitoring

For troubleshooting purposes, you might want to analyze packets flowing over the network. To capture packets (that is, store a copy of packets on a local hard drive) for analysis, you could attach a _network sniffer_ to a hub. Because a hub sends bits received on one port out all other ports, the attached network sniffer sees all traffic entering the hub.  
  
Although several standalone network sniffers are on the market, a low-cost way to perform packet capture and analysis is to use software such as [Wireshark](http://www.wireshark.org/), as shown in Figure 4-21.  
  

![Screenshot of Wireshark Packet-Capture Software window is shown. The screen displays the menu bar and taskbar options at the top. The content area shows a table with multiple rows of data with respect to the column header that reads the number, time, source, destination, protocol, and info. Two rows in the table are shown in Port Monitoring mode. The troubleshooting details are displayed below.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig21.jpg)

Figure 4-21: Example: Wireshark Packet-Capture Software

  
A challenge arises, however, if you connect your network sniffer (for example, a laptop running the Wireshark software) to a switch port rather than a hub port. Because a switch, by design, forwards frames out ports containing the frames' destination addresses, a network sniffer attached to one port would not see traffic destined for a device connected to a different port.  
  
Consider Figure 4-22. Traffic enters a switch on port 1 and, based on the destination MAC addresses, exits via port 2. However, a network sniffer is connected to port 3 and is unable to see (and therefore capture) the traffic flowing between ports 1 and 2.  
  

![Diagram of a Network Sniffer Unable to Capture Traffic is shown. PC and PC with packet capture software on either side at the bottom is shown connected to a switch at the top. A connection is shown at the top switch to port 1 (ingress port). Port 2 of the switch is connected to PC on the left and Port 3 of the switch is connected to PC with packet capture software. Two downward arrows are shown flowing from the top of the switch to port 1 of the switch and port 2 to PC.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig22.jpg)

Figure 4-22: Example: Network Sniffer Unable to Capture Traffic

  
Fortunately, some switches support a _port mirroring_ feature, which makes a copy of traffic seen on one port and sends that duplicated traffic out another port (to which a network sniffer could be attached). As shown in Figure 4-23, the switch is configured to mirror traffic on port 2 to port 3. This allows a network sniffer to capture the packets that need to be analyzed. Depending on the switch, locally captured traffic could be forwarded to a remote destination for centralized analysis of that traffic.  
  

![Diagram of a Network Sniffer with Port Mirroring Configured on the Switch is shown. Two computers PC and PC with packet capture software on either side at the bottom is shown connected to a switch at the top. A connection is shown at the top switch to port 1 (ingress port). Port 2 of the switch is connected to PC on the left represents mirrored port and Port 3 of the switch is connected to PC with packet capture software represents Copy of Original Frame. Three downward arrows are shown flowing from the top of the switch to port 1 of the switch, port 3 2 to PC and port 3 to PC with Packet Capture Software.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig23.jpg)

Figure 4-23: Example: Network Sniffer with Port Mirroring Configured on the Switch

#### Port Mirroring Configuration

Example 4-4 shows a sample configuration from a Cisco Catalyst switch that captures all the frames coming in on port Gig 0/1 and forwards them to port Gig 0/3.  
  
**Example 4-4** Port Mirroring Configuration
```
SW1(config)# **monitor session 1 source interface Gi0/1**  
SW1(config)# **monitor session 1 destination interface Gi0/3**
```

#### User Authentication

For security purposes, some switches require users to _authenticate_ themselves (that is, provide credentials, such as a username and password, to prove who they are) before gaining access to the rest of the network. A standards-based method of enforcing user authentication is IEEE 802.1X.  
  
With 802.lX enabled, a switch requires a client to authenticate before communicating on the network. After the authentication occurs, a key is generated that is shared between the client and the device to which it attaches (for example, a wireless LAN controller or a Layer 2 switch). The key then encrypts traffic coming from and being sent to the client.  
  
In Figure 4-24, you see the three primary components of an 802.1X network, which are described in the following list:  
  

![Diagram of three primary components of an 802.1X network is shown. The three components from left to right reads supplicant, authenticator, and the authentication server. A laptop, a switch of 2 layers, and a PC are shown connected under each component respectively. A double-headed arrow from the laptop to the PC is shown below labeled 802.1X Authentication. A double-headed arrow from the laptop to the switch is labeled Key Management and from the switch to the PC is labeled Key Distribution. Another double-headed arrow from the laptop to the switch is labeled Key Management and from the laptop to the switch is labeled Secured Data.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig24.jpg)

Figure 4-24: 802.1X User Authentication

- **Supplicant:** The device that wants to gain access to the network.
- **Authenticator:** The authenticator forwards the supplicant's authentication request on to an authentication server. After the authentication server authenticates the supplicant, the authenticator receives a key that is used to communicate securely during a session with the supplicant.
- **Authentication server:** The authentication server (for example, a Remote Authentication Dial In User Service [RADIUS] server) checks a supplicant's credentials. If the credentials are acceptable, the authentication server notifies the authenticator that the supplicant is allowed to communicate on the network. The authentication server also gives the authenticator a key that can be used to securely transmit data during the authenticator's session with the supplicant.

An even more sophisticated approach to admission control is the Network Admission Control (NAC) feature offered by some authentication servers. Beyond just checking credentials, NAC can check characteristics of the device seeking admission to the network. The client's operating system (OS) and version of antivirus software are examples of these characteristics.

#### Management Access and Authentication

To configure a managed switch, you could use Secure Shell (SSH) or connect directly to the console port of the switch. An unmanaged switch is one that does not support the use of an IP address or a console port to connect to for management purposes. When possible, using a separate network for management of a managed switch is desired. This is referred to as _out-of-band_ (OOB) management when the management traffic is kept on a separate network than the user traffic. To use remote SSH access, SSH must be enabled on the switch and the switch must have an IP address and default gateway configured so it can reply to the SSH requests when the administrator using SSH is not on the same local network as the switch. Example 4-5 shows a sample configuration for IP and management access on a Cisco Catalyst switch.  
  
**Example 4-5** Management Access
```
! Move to the logical Layer 3 interface that will  
! receive the management IP address for the switch  
SW1(config)# **interface vlan 1**  
  
! Configure an IP address that is available for the  
! switch to use  
SW1(config-if)# **ip address 172.16.55.123 255.255.255.0**  
SW1(config-if)# **exit**  
  
! Configure a domain name, required for creating the  
! keys used for SSH cryptography  
SW1(config)# **ip domain-name pearson.com**  
  
! Create the public/private key pair SSH can use  
SW1(config)# **crypto key generate rsa modulus 1024**  
  
! Specify the version of SSH to allow  
SW1(config)# **ip ssh version 2**  
  
! Create a user account on the local switch  
SW1(config)# **username admin privilege 15 secret pears0nR0cks!**  
  
! Move to the logical VTY lines used for SSH access  
SW1(config)# **line vty 0 15**  
  
! Allow only SSH on the logical range 16 VTY lines (0 - 15)  
SW1(config-line)# **transport input ssh**  
  
! Require using an account from the local switch to log in  
SW1(config-line)# **login local**  
SW1(config-line)# **exit**  
  
! Set the default gateway the switch can use when communicating  
! over an SSH session with an administrator who is on a different  
! network than the switch's interface VLAN 1  
SW1(config)# **ip default-gateway 172.16.55.1**  
  
! Move to the console port of the switch  
SW1(config)# **line console 0**  
  
! Require authentication using the local switch before allowing  
! access to the switch through the console port  
SW1(config-line)# **login local**

```

### NOTE:
The virtual terminal (VTY) lines (lines 0–15 in the example) allow for 16 simultaneous connections to the switch by administrators. If more simultaneous connections are required, additional virtual terminal lines could be configured on the switch.

Cisco has another first-hop proprietary redundancy protocol named _Gateway Load Balancing Protocol_ (GLBP). Whereas GLBP and HSRP are Cisco proprietary solutions, Virtual Router Redundancy Protocol (VRRP) and Common Address Redundancy Protocol (CARP) are open standard options for first-hop redundancy.

#### First-Hop Redundancy

Many devices, such as PCs, are configured with a default gateway. The _default gateway_ parameter identifies the IP address of a next-hop router. As a result, if that router were to become unavailable, devices that relied on the default gateway's IP address would be unable to send traffic off their local subnet, even if a backup router exists.  
  
Fortunately, a variety of technologies are available for providing first-hop redundancy. One such technology is Hot Standby Router Protocol (HSRP), which is a Cisco proprietary protocol. HSRP can run on routers or multilayer switches.  
  
HSRP uses virtual IP and virtual MAC addresses. One router, known as the _active router_, services requests destined for the virtual IP and virtual MAC. Another router, known as the _standby router_, can service such requests in the event the active router becomes unavailable. Figure 4-25 illustrates a sample HSRP topology.  
  

![Example of an HSRP topology is shown. The example shows an oval region labeled "HSRP Group 10" which has an active router labeled R1, a virtual router labeled virtual, and a standby router labeled "R2." An Ethernet bus is connected to the port Fa 0/0 of R1 with IP Address 172.16.1.1, Virtual with IP Address 172.16.1.3, and port e 0/0 of R2 with IP Address 172.16.1.2. The Ethernet bus, in turn, is connected to a PC labeled workstation A with Next-Hop Gateway of 172.16.1.3.](https://s3.amazonaws.com/jigyaasa_content_static/Image4/04fig25.jpg)

Figure 4-25: Sample HSRP Topology

  
Notice that router R1 is acting as the active router, and router R2 is acting as the standby router. When workstation A sends traffic destined for a remote network, it sends traffic to its default gateway of 172.16.1.3, which is the virtual IP address shared by the HSRP routers. When router R1 is the active router, it assumes the virtual IP and virtual MAC, and it forwards the traffic off the local network. However, if R2 notices that R1 has become unavailable (because hello messages are no longer received from router R1), R2 transitions to the active router role and assumes the virtual IP and virtual MAC. With default timer settings, the time required to fail over to router R2 is approximately 10 seconds. However, timers can be adjusted such that the failover time is as little as 1 second.

#### Other Switch Features

Switch features, such as those previously described, vary widely by manufacturer, and some switches offer a variety of security features. For example, MAC filtering might be supported, which allows traffic to be permitted or denied based on a device's MAC address. Other types of traffic filtering might also be supported, based on criteria such as IP address information (for multilayer switches).  
  
For monitoring and troubleshooting purposes, interface _diagnostics_ might be accessible. This diagnostic information might contain information including various error conditions—for example, late collisions or cyclic redundancy check (CRC) errors, which might indicate a duplex mismatch.  
  
Some switches also support _quality of service_ (QoS) settings. QoS can forward traffic based on the traffic's priority markings. Also, some switches have the ability to perform marking and remarking of traffic priority values.

# 4.3 Real-World Case Study

Acme, Inc., has made some decisions regarding the setup of its LAN. For connections from the client machines to the switches in the wiring closets (IDF), it will use unshielded twisted-pair Category 5 cabling with the switch ports configured as access ports and set to 100Mbps to match the Fast Ethernet capabilities of the client computers that will be connecting to the switch.  
  
Multiple VLANs will be used. The computers that are being used by the Sales department will be connected to ports on a switch that are configured as access ports for the specific VLAN for Sales. Computers used by Human Resources will connect to switch ports that are configured as access ports for the Human Resources VLAN. There will be separate IP subnetworks associated with each of the VLANs.  
  
To provide a fault-tolerant default gateway for the clients in each of the VLANs, a first-hop redundancy protocol will be used, such as HSRP, GLBP, or VRRP.  
  
The fiber connections that will go vertically through the building and connect the switches in the IDFs to the MDF in the basement will be running at 1Gbps each, and multiple fiber cables will be used. Link Aggregation Control Protocol will be used for these vertical connections to make the multiple fiber links work together as part of one logical EtherChannel interface. For the LACP connections between the IDFs and MDF to support multiple VLANs, the LAG will be configured as a trunk using 802.1Q tagging. Routing between the VLANs will be done by multilayer switches that are located near the MDF.  
  
Spanning tree will be enabled on the switches so that in the event of parallel paths between switches, a Layer 2 loop can be prevented.  
  
To support IP-based telephones in the offices, the switches will also provide Power over Ethernet, which can supply power to the IP phones over the Ethernet cables that run between the switch in the IDF and the IP telephones.  
  
If protocol analysis needs to be done, the switches that will be purchased need to support port mirroring so that frames from one port can be captured and forwarded to an alternate port for analysis.  
  
To authenticate devices that are connecting to the switch ports, 802.1X can be used. To authenticate administrators who are connecting to switches for management, authentication can be forced at the logical VTY lines. SSH will be enabled and enforced because it is a secure management protocol. The switches will be given their own IP address, in addition to a default gateway to use so that they can be remotely managed. Local user accounts will be created on the switches so that local authentication can be implemented as each administrator connects either to the console or via SSH.

# 4.4 Summary

Here are the main topics covered in this lesson:  

- The origins of Ethernet, including a discussion of Ethernet's CSMA/CD features.
- A variety of Ethernet standards were contrasted in terms of media type, network bandwidth, and distance limitation.
- Various features that might be available on modern Ethernet switches. These features include VLANs, trunking, STP, link aggregation, PoE, port monitoring, user authentication, and first-hop redundancy.
![[Pasted image 20230716165320.png]]

# Glossary

#### Ethernet
Ethernet is a Layer 1 technology developed by Xerox and encompasses a variety of standards that specify various media types, speeds, and distance limitations.

#### collision
A collision occurs when two devices on an Ethernet network simultaneously transmit a frame. Because an Ethernet segment cannot handle more than one frame at a time, both frames become corrupted.

#### carrier-sense multiple access/collision detect (CSMA/CD)
Used on an Ethernet network to help prevent a collision from occurring and to recover if a collision does occur. CSMA/CD is only needed on half-duplex connections.

#### full duplex
This connection allows a device to simultaneously transmit and receive data.

#### half duplex
A half-duplex connection allows a device to either receive or transmit data at any one time. However, a half-duplex device cannot simultaneously transmit and receive.

#### virtual LAN (VLAN)
A single broadcast domain, representing a single subnet. Typically, a group of ports on a switch is assigned to a single VLAN. For traffic to travel between two VLANs, that traffic needs to be routed.

#### trunk
In the context of an Ethernet network, this is a single physical or logical connection that simultaneously carries traffic for multiple VLANs. However, a trunk also refers to an interconnection between telephone switches, in the context of telephony.

#### Spanning Tree Protocol (STP)
Defined by the IEEE 802.1D standard, STP allows a network to have redundant Layer 2 connections while logically preventing a loop, which could lead to symptoms such as broadcast storms and MAC address table corruption.

#### root port
In an STP topology, every nonroot bridge has a single root port, which is the port on that switch that is closest to the root bridge, in terms of cost.

#### designated port
In an STP topology, every network segment has a single designated port, which is the port on that segment that is closest to the root bridge, in terms of cost. Therefore, all ports on a root bridge are designated ports.

#### nondesignated port
In STP terms, nondesignated ports block traffic to create a loop-free topology.

#### link aggregation
As defined by the IEEE 802.3ad standard, link aggregation allows multiple physical connections to be logically bundled into a single logical connection.

#### Power over Ethernet (PoE)
Defined by the IEEE 802.3af and 802.3at standards, PoE allows an Ethernet switch to provide power to an attached device (for example, a wireless access point, security camera, or IP phone) by applying power to the same wires in a UTP cable that are used to transmit and receive data.

#### supplicant
In a network using 802.1X user authentication, a supplicant is the device that wants to gain access to a network.

#### authenticator
In a network using 802.1X user authentication, an authenticator forwards a supplicant's authentication request on to an authentication server. After the authentication server authenticates the supplicant, the authenticator receives a key that is used to communicate securely during a session with the supplicant.

#### authentication server
In a network using 802.1X user authentication, an authentication server (typically, a RADIUS server) checks a supplicant's credentials. If the credentials are acceptable, the authentication server notifies the authenticator that the supplicant is allowed to communicate on a network. The authentication server also gives the authenticator a key that can be used to securely transmit data during the authenticator's session with the supplicant.