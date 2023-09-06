# 3.1 Media
The media might be physical, such as a copper or fiber-optic cable. Alternatively, the media might be the air, through which radio waves propagate (as is the case with wireless networking technologies).  
  
This section contrasts various media types, including physical and wireless media. Although some wireless technologies are covered here, be aware that wireless technologies are examined more thoroughly in Lesson 8, "Wireless Technologies."

===============================================================
## Coaxial Cable

Coaxial cable (referred to as _coax_) consists of two conductors. As illustrated in Figure 3-1, one of the conductors is an inner insulated conductor. This inner conductor is surrounded by another conductor. This second conductor is sometimes made of a metallic foil or woven wire.  
  
![The figure shows a structure of a coaxial cable having four layers.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig01.jpg)
Figure 3-1: Coaxial Cable

Because the inner conductor is shielded by the metallic outer conductor, coaxial cable is resistant to electromagnetic interference (EMI). For example, EMI occurs when an external signal is received on a wire and might result in a corrupted data transmission. As another example, EMI occurs when a wire acts as an antenna and radiates electromagnetic waves, which might interfere with data transmission on another cable. Coaxial cables have an associated characteristic impedance that needs to be balanced with the device (or terminator) with which the cable connects.

The following list details three of the most common types of coaxial cables:  
**RG prefix used in coaxial cable type stands for radio guide**

- **RG-59:** Typically used for short-distance applications, such as carrying composite video between two nearby devices. This cable type has loss characteristics such that it is not right for long-distance applications. RG-59 cable has a characteristic impedance of 75 Ohms.
- **RG-6:** Used by local cable companies to connect individual homes to the cable company's distribution network. Like RG-59 cable, RG-6 cable has a characteristic impedance of 75 Ohms.
- **RG-58:** Has loss characteristics and distance limitations like those of RG-59. However, the characteristic impedance of RG-58 is 50 ohms, and this type of coax was popular with early 10BASE2 Ethernet networks (which are discussed in Lesson 4, "Ethernet Technology").

Although RG-58 coaxial cable was commonplace in early computer networks (in 10BASE2 networks), coaxial cable's role in modern computer networks is as the media used by cable modems. Cable modems are commonly installed in residences to provide high-speed Internet access over the same connection used to receive multiple television stations.

### Connectors:
Common connectors used on coaxial cables are as follows:  

- **BNC:** A Bayonet Neill-Concelman (BNC) connector (_British Naval-Connector_ in some literature) can be used for a variety of applications, including as a connector in a 10BASE2 Ethernet network. A BNC coupler could be used to connect two coaxial cables together back to back.
- **F-connector:** An F-connector is often used for cable TV (including cable modem) connections. Notice that some refer to it is simply as **F-type, including CompTIA.**

Figure 3-2 shows what both of these connectors look like.  
![The figure shows a BNC connector and F-connector on the left and right, respectively.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig02.jpg)

===============================================================
## Twisted-Pair Cable

Today's most popular LAN media type is twisted-pair cable, where individually insulated copper strands are intertwined. Two categories of twisted-pair cable include shielded twisted pair (STP) and unshielded twisted pair (UTP). A UTP coupler could be used to connect two UTP cables, back to back. Also, for adherence to fire codes, you might need to select plenum cable versus nonplenum cable.  
  
To define industry-standard pinouts and color coding for twisted-pair cabling, the TIA/EIA-568 standard was developed. The first iteration of the TIA/EIA-568 standard has come to be known as the _TIA/EIA-568-A_ standard, which was released in 1991.

#### Shielded Twisted Pair

If wires in a cable are not twisted or shielded, that cable can act as an antenna, which might receive or transmit EMI. To help prevent this type of behavior, the wires (which are individually insulated) can be twisted together in pairs.  
  
If the distance between the twists is less than a quarter of the wavelength of an electromagnetic waveform, the twisted pair of wires will not radiate that wavelength or receive EMI from that wavelength (in theory, if the wires were perfect conductors). However, as frequencies increase, wavelengths decrease.  
  
One option of supporting higher frequencies is to surround a twisted pair in a metallic shielding, similar to the outer conductor in a coaxial cable. This type of cable is referred to as a _shielded twisted-pair_ (STP) _cable_.  
  
Figure 3-3 shows an example of STP cable. These outer conductors shield the copper strands from EMI; however, the addition of the metallic shielding adds to the expense of STP.  
  

![The figure shows a shielded twisted pair cable. The cable has an outer conductor that holds four copper strands. The strands are covered by an inner conductor. The colors of the strands are as follows: green and white, orange and white, brown and white, and blue and white.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig03.jpg)

Figure 3-3: Shielded Twisted Pair

#### Unshielded Twisted Pair

Another way to block EMI from the copper strands making up a twisted-pair cable is to twist the strands more tightly (that is, more twists per centimeter). With these strands wrapped around each other, the wires insulate each other from EMI.  
  
Figure 3-4 illustrates an example of UTP cable. Because UTP is less expensive than STP, it has grown in popularity since the mid-1990s to become the media of choice for most LANs.  
  

![The figure shows an unshielded twisted pair cable. The cable has an outer conductor that holds four copper strands. The colors of the strands are as follows: blue/blue and white, brown/brown and white, orange/orange and white, and green/green and white.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig04.jpg)

Figure 3-4: Unshielded Twisted Pair

  
UTP cable types vary in their data carrying capacity. Common categories of UTP cabling include the following:  

- **Category 3:** Category 3 (Cat 3) cable was used in older Ethernet 10BASE-T networks, which carried data at a rate of 10Mbps (where Mbps stands for megabits per second, meaning millions of bits per second). However, Cat 3 cable can carry data at a maximum rate of 16Mbps, as seen in some older Token Ring networks.
- **Category 5:** Category 5 (Cat 5) cable is commonly used in Ethernet 100BASE-TX networks, which carry data at a rate of 100Mbps. However, Cat 5 cable can carry ATM traffic at a rate of 155Mbps. Most Cat 5 cables consist of four pairs of 24-gauge wires. Each pair is twisted, with a different number of twists per meter. However, on average, one pair of wires has a twist every 5 cm.
- **Category 5e:** Category 5e (Cat 5e) cable is an updated version of Cat 5 and is commonly used for 1000BASE-T networks, which carry data at a rate of 1Gbps. Cat 5e cable offers reduced crosstalk, as compared to Cat 5 cable.
- **Category 6:** Like Cat 5e cable, Category 6 (Cat 6) cable is commonly used for 1000BASE-T Ethernet networks. Some Cat 6 cable is made of thicker conductors (for example, 22-gauge or 23-gauge wire), although some Cat 6 cable is made from the same 24-gauge wire used by Cat 5 and Cat 5e. Cat 6 cable has thicker insulation and offers reduced crosstalk, as compared with Cat 5e.
- **Category 6a:** Category 6a (Cat 6a), or augmented Cat 6, supports twice as many frequencies as Cat 6 and can be used for 10GBASE-T networks, which can transmit data at a rate of 10 billion bits per second (10 Gbps).

Although other wiring categories exist, those presented in the previous list are the categories most commonly seen in modern networks.  
  
Most UTP cabling used in today's networks is considered to be _straight-through_, meaning that the RJ-45 jacks at each end of a cable have matching pinouts. For example, pin 1 in an RJ-45 jack at one end of a cable uses the same copper conductor as pin 1 in the RJ-45 jack at the other end of a cable.  
  
However, some network devices cannot be interconnected with a straight-through cable. For example, consider two PCs interconnected with a straight-through cable. Because the network interface cards (NICs) in these PCs use the same pair of wires for transmission and reception, when one PC sends data to the other PC, the receiving PC would receive the data on its transmission wires, rather than its reception wires. For such a scenario, you can use a crossover cable, which swaps the transmit and receive wire pairs between the two ends of a cable.

### CROSSOVER CABLE
A crossover cable for Ethernet devices is different from a crossover cable used for a digital T1 circuit (as discussed in Lesson 7, "Wide Area Networks (WANs) "). Specifically, an Ethernet crossover cable has a pin mapping of 1 > 3, 2 > 6, 3 > 1, and 6 > 2, whereas a T1 crossover cable has a pin mapping of 1 > 4, 2 > 5, 4 > 1, and 5 > 2. Another type of cable is the rollover cable, which is used to connect to a console port to manage a device such as a router or switch. The pin mapping for a rollover cable is 1 < > 8, 2 < > 7, 3 < > 6, 4 < > 5. The end of the cable looks like an RJ-45 eight-pin connector.

### MEDIA DEPENDENT
A traditional port found in a PC's NIC is called a _media-dependent interface_ (MDI). If a straight-through cable connects a PC's MDI port to an Ethernet switch port, the Ethernet switch port needs to swap the transmit pair of wires (that is, the wires connected to pins 1 and 2) with the receive pair of wires (that is, the wires connected to pins 3 and 6).  
  
Therefore, a traditional port found on an Ethernet switch is called a _media-dependent interface crossover_ (MDIX), which reverses the transmit and receive pairs. However, if you want to interconnect two switches, where both switch ports used for the interconnection were MDIX ports, the cable would need to be a crossover cable.  
  
Fortunately, most modern Ethernet switches have ports that can automatically detect whether they need to act as MDI ports or MDIX ports and make the appropriate adjustments. This eliminates the necessity of using straight-through cables for some Ethernet switch connections and crossover cables for other connections. With this _Auto-MDIX_ feature, you can use either straight-through cables or crossover cables.

### CONNECTORS:
Common connectors used on twisted-pair cables are as follows:  

- **RJ-45:** A type 45 registered jack (RJ-45) is an eight-pin connector found in most Ethernet networks. However, most Ethernet implementations only use four of the eight pins.
- **RJ-11:** A type 11 registered jack (RJ-11) has the capacity to be a six-pin connector. However, most RJ-11 connectors have only two or four conductors. An RJ-11 connector is found in most home telephone networks. However, most home phones only use two of the six pins.
- **DB-9 (RS-232):** A nine-pin D-subminiature (DB-9) connector is an older connector used for low-speed asynchronous serial communications, such as a PC to a serial printer, a PC to a console port of a router or switch, or a PC to an external modem. Do not confuse the DB-9 with a DB-25. The DB-25 connector was also used for the serial or parallel ports of early personal computers.

Figure 3-5 shows what these connectors look like.  
![Illustrations of RJ-45 connector, RJ-11 connector, and DB-9 (RS-232) connector are shown.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig05.jpg)
Figure 3-5: Twisted-Pair Cable Connectors

#### Plenum Versus Nonplenum Cable

If a twisted-pair cable is to be installed under raised flooring or in an open-air return, fire codes must be considered. For example, imagine that there was a fire in a building. If the outer insulation of a twisted-pair cable caught on fire or started to melt, it could release toxic fumes. If those toxic fumes were released in a location such as an open-air return, those fumes could be spread throughout a building, posing a huge health risk.  
  
To mitigate the concern of pumping poisonous gas throughout a building's heating, ventilation, and air conditioning (HVAC) system, _plenum_ cabling can be used. The outer insulator of a plenum twisted-pair cable is not only fire retardant; some plenum cabling uses a fluorinated ethylene polymer (FEP) or a low-smoke polyvinyl chloride (PVC) to minimize dangerous fumes.

===============================================================

## Fiber-Optic Cable
An alternative to copper cabling is fiber-optic cabling, which sends light (instead of electricity) through an optical fiber (typically made of glass). Using light instead of electricity makes fiber optics immune to EMI. Also, depending on the Layer 1 technology being used, fiber-optic cables typically have greater range (that is, a greater maximum distance between networked devices) and greater data-carrying capacity.  
  
Lasers are often used to inject light pulses into a fiber-optic cable. However, lower-cost light-emitting diodes (LED) are also on the market. Fiber-optic cables are generally classified according to their diameter and fall into one of two categories: multimode fiber (MMF) and single-mode fiber (SMF).  
  
The wavelengths of light also vary between MMF and SMF cables. Usually, wavelengths of light in a MMF cable are in the range of 850–1300 nm, where nm stands for nanometers. A nanometer is one billionth of a meter. Conversely, the wavelengths of light in a SMF cable use usually in the range of 1310–1550 nm. A fiber coupler could be used to connect two fiber cables, back to back.

#### Multimode Fiber

When a light source, such as a laser, sends light pulses into a fiber-optic cable, what keeps the light from simply passing through the glass and being dispersed into the surrounding air? The trick is that fiber-optic cables use two different types of glass. There is an inner strand of glass (that is, a _core_) surrounded by an outer _cladding_ of glass, similar to the construction of the previously mentioned coaxial cable.  
  
The light injected by a laser (or LED) enters the core, and the light is prevented from leaving that inner strand and going into the outer cladding of glass. Specifically, the indices of refraction of these two different types of glass are so different that if the light attempts to leave the inner strand, it hits the outer cladding and bends back on itself.  
  
To better understand this concept, consider a straw in a glass of water, as shown in Figure 3-6. Because air and water have different indices of refraction (that is, light travels at a slightly different speed in air and water), the light that bounces off of the straw and travels to our eyes is bent by the water's index of refraction. When a fiber-optic cable is manufactured, dopants are injected into the two types of glasses, making up the core and cladding to give them significantly different indices of refraction, thus causing any light attempting to escape to be bent back into the core.  
  

![Figure shows a glass of water with a straw. The visibility position of straw in the air and in the water are different.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig06.jpg)

Figure 3-6: Example: Refractive Index

  
The path that light travels through a fiber-optic cable is called a _mode of propagation_. The diameter of the core in a multimode fiber is large enough to permit light to enter the core at different angles, as depicted in Figure 3-7. If light enters at a steep angle, it bounces back and forth much more frequently on its way to the far end of the cable as opposed to the light enters perpendicular to the end of the cable. If pulses of light representing different bits travel down the cable using different modes of propagation, it is possible that the bits (that is, the pulses of light representing the bits) will arrive out of order at the far end (where the pulses of light, or absence of light, are interpreted as binary data by photoelectronic sensors).  
  

![The figure showing the propagation of light in a multimode fiber. The illustration shows two concentric horizontal cylinders. The outer cylinder is named as cladding and the inner cylinder is named as core. A pulse of light passes through the fiber. The pulse of light representing the first and third bit intersects the core. The pulse of light representing the second bit is found perpendicular to the core.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig07.jpg)

Figure 3-7: Light Propagation in Multimode Fiber

  
For example, perhaps the pulse of light representing the first bit intersected the core at a steep angle and bounced back and forth many times on its way to the far end of the cable, while the light pulse representing the second bit intersected the core perpendicularly and did not bounce back and forth very much. With all of its bouncing, the first bit has to travel further than the second bit, which might cause the bits to arrive out of order. Such a condition is known as _multimode delay distortion_. To mitigate the issue of multimode delay distortion, MMF typically has shorter distance limitations, as opposed to SMF.

#### Single-Mode Fiber

SMF eliminates the issue of multimode delay distortion by having a core with a diameter so small that it only permits one mode (that is, one path) of propagation, as shown in Figure 3-8. With the issue of multimode delay distortion mitigated, SMF typically has longer distance limitations than MMF.  
  

![An illustration depicts the propagation of light in a single-mode fiber. The illustration shows two concentric horizontal cylinders. The outer cylinder is named "cladding" and the inner cylinder is named "core". A light path passes through the center of the fiber.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig08.jpg)

Figure 3-8: Light Propagation in Single-Mode Fiber

  
A potential downside to SMF, however, is cost. Because SMF has to be manufactured to very exacting tolerances, you usually pay more for a given length of fiber-optic cabling. However, for some implementations, where greater distances are required, the cost is an acceptable trade-off to reach greater distances.  
  
Some common connectors used on fiber-optic cables are as follows:  

- **ST:** A _straight tip_ (ST) _connector_ is sometimes referred to as a _bayonet connector_, because of the long tip extending from the connector. ST connectors are most commonly used with MMF. An ST connector connects to a terminating device by pushing the connector into the terminating equipment and then twisting the connector housing to lock it in place.
- **SC:** Different literature defines an SC connector as _subscriber connector_, _standard connector_, or _square connector_. The SC connector is connected by pushing the connector into the terminating device, and it can be removed by pulling the connector from the terminating device. The connector has slight variants within the industry, with the major types being APC, UPC, and MTRJ. Always consult with the vendor or IT staff member regarding the exact requirements.
- **LC:** A _Lucent connector_ (LC) connects to a terminating device by pushing the connector into the terminating device, and it can be removed by pressing the tab on the connector and pulling it out of the terminating device.
- **MTRJ:** The most unique characteristic of a _mechanical transfer registered jack_ (MTRJ) connector is that two fiber strands (a transmit strand and a receive strand) are included in a single connector. An MTRJ connector is connected by pushing the connector into the terminating device, and it can be removed by pulling the connector from the terminating device.

Figure 3-9 shows what these connectors look like.  
  

![Four representations show the common types of connectors used on fiber-optic cables. The first representation shows the ST connector. Description beside it reads, the ST connector uses a half-twist bayonet type of lock. The second representation shows the SC connector. Description beside it reads, the SC uses a push-pull connector similar to common audio and video plugs and sockets. The third representation shows the LC connector. Description beside it reads, LC connectors have a flange on top, similar to an RJ-45 connector, that aids secure connection. The fourth representation shows the MT-RJ connector. Description beside it reads, MT-RJ is a popular connector for two fibers in a very small form factor.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig09.jpg)

Figure 3-9: Common Fiber-Optic Connectors

===============================================================

Here are some of the common copper cable and fiber-optic cable connectors:

- **RJ-45:** A twisted-pair copper cable connector that has eight pins and is commonly found in most Ethernet networks. However, most Ethernet implementations only use four of the eight pins.
- **MTRJ:** A fiber-optic cable connector that includes two fibers (a transmit strand and a receive strand) in a very small form factor. It is connected by pushing the connector into the terminating device and it can be removed by pulling the connector from the terminating device.
- **SC:** A fiber-optic cable connector that uses a push-pull connector similar to common audio and video plugs and sockets. It is connected by pushing the connector into the terminating device and it can be removed by pulling the connector from the terminating device.
- **LC:** A fiber-optic cable connector that has a flange on top that aids secure connection. It connects to a terminating device by pushing the connector into the terminating device and it can be removed by pressing the tab on the connector and pulling it out of the terminating device.
- **F-connector:** An F-connector is a coaxial cable connector that is often used for cable TV or cable modem connections.
- **DB-9 (RS-232):** A 9-pin D-subminiature (DB-9) is an older twisted-pair copper cable connector used for low speed asynchronous serial communications, such as a PC to a serial printer.

===============================================================

#### Fiber Connector Polishing Styles

Fiber-optic cables have different types of mechanical connections. The type of connection impacts the quality of the fiber-optic transmission. Listed from basic to better, the options include Physical Contact (PC), Ultra Physical Contact (UPC), and Angled Physical Contact (APC), which refer to the polishing styles of fiber-optic connectors. The different polishing styles of the fiber-optic connectors result in different performance of the connector. The less back reflection, the better the transmission. The PC back reflection is –40 dB, the UPC back reflection is around –55 dB, and the APC back reflection is about –70 dB.

#### Media Converters

There may be times when the media needs to be converted. To do this, a media converter could be used. Examples may include single-mode fiber to Ethernet, multimode fiber to Ethernet, fiber to coaxial, and single-mode to multimode fiber.

#### Cable Distribution

After deciding on what type of media you are going to use in your network (for example, UTP, STP, MMF, or SMF), you should install that media as part of an organized cable distribution system. Typically, cable distribution systems are hierarchical in nature.  
  
Consider the example profiled in Figure 3-10. In this example, cable from end-user offices runs back to common locations within the building. These locations are sometimes referred to as _wiring closets_. Cables in these locations might terminate in a _patch panel_. This patch panel might consist of some sort of cross-connect block wired into a series of ports (for example, RJ-45 ports), which can be used to quickly interconnect cables coming from end-user offices with a network device, such as an Ethernet switch. A building might have multiple patch panels (for example, on different floors of a building). These common locations, where cables from nearby offices terminate, are often called _intermediate distribution frames_ (IDFs).  
  

![A cable distribution system shows a building that has a block labeled "MDF" at the top and three blocks labeled "IDF" at the bottom. MDF is connected to a cloud labeled "carrier" at its top and to the three IDF's at its bottom. Each IDF is connected to a laptop.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig10.jpg)

Figure 3-10: Example: Cable Distribution System

  
The two most popular types of cross-connect blocks found in an IDF are detailed here:  

- **66 block:** A 66 block, as shown in Figure 3-11, was traditionally used in corporate environments for cross-connecting phone system cabling. As 10Mbps LANs grew in popularity, in the late 1980s and early 1990s, these termination blocks were used to cross-connect Cat 3 UTP cabling. The electrical characteristics (specifically, crosstalk) of a 66 block, however, do not support higher-speed LAN technologies, such as 100Mbps Ethernet networks.  
      
    
    ![A figure of a 66 block is shown.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig11.jpg)
    
    Figure 3-11: 66 Block
    
  
- **110 block:** Because 66 blocks are subject to too much crosstalk (that is, interference between different pairs of wires) for higher-speed LAN connections, 110 blocks, an example of which is provided in Figure 3-12, can terminate a cable (for example, a Cat 5 cable) being used for those higher-speed LANs.  
      
    
    ![A figure of a 110 block is shown.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig12.jpg)
    
    Figure 3-12: 110 Block
    

This centralized distribution frame, which connects out to multiple IDFs, is called the _main distribution frame_ (MDF).  
  
Another component you might use is a fiber optic patch panel. This is often termed a fiber distribution panel. You use this to organize and distribute optical cables. It also allows you to terminate cable elements and provides a secure, organized chamber for housing connectors and splice units.  
  
With such a wide variety of copper and fiber cabling used by different network devices, you might need one or more _media converters_. Examples of media converters include the following:  

- Fiber (MMF or SMF) to Ethernet
- Fiber to coaxial
- SMF to MMF

===============================================================

#### Wireless Technologies

Not all media is physical, as is the case of wireless network technologies. This book dedicates Lesson 8 to these technologies. However, for now, you just need to understand the basics.  
  
Consider the sample wireless topology presented in Figure 3-13. Notice that wireless clients gain access to a wired network by communicating via radio waves with a wireless access point (AP). The AP is then hardwired to a LAN.  
  

![A wireless network topology with the following components is displayed: three laptops labeled as wireless clients, wireless access point, and Ethernet switch. The three wireless clients are connected to the wireless access point via radio waves. The Ethernet switch is connected to the wireless access point through an Ethernet cable. A rightward facing arrow below the switch reads, to a wired network.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig13.jpg)

Figure 3-13: Example: Wireless Network Topology

  
As discussed in Lesson 8, wireless LANs include multiple standards that support various transmission speeds and security features. However, you need to understand, at this point, that all wireless devices connecting to the same AP are considered to be on the same _shared network segment_, which means that only one device can send data to and receive data from an AP at any one time.

#### Technologies for the Internet of Things

Many wireless technologies (or related to wireless) come in to play to make the Internet of Things (IoT) a reality. IoT refers to the trend today to connect everyday objects to the Internet in order to make them "smart." In my home, I speak to my Amazon Echo speaker in order to have it control the lights, for example. This Internet-connected speaker and the lights are perfect examples of IoT in action.  
  
Here are key technologies you should be aware of that help make the modern IoT a reality:  

- **Z-Wave:** A wireless communications protocol used primarily for home automation. It is a mesh network using low-energy radio waves to communicate from appliance to appliance. Z-Wave is found with devices such as lighting control systems, security systems, thermostats, windows, locks, swimming pools, and garage door openers.
- **Ant+:** A wireless protocol for monitoring sensor data such as a person's heart rate or a car's tire pressure, as well as for controlling systems such as indoor lighting and entertainment appliances such as televisions. ANT+ is designed and maintained by the ANT+ Alliance, which is owned by Garmin.
- **Bluetooth:** As discussed in Lesson 1, "Computer Network Fundamentals," Bluetooth is a wireless technology that allows devices to communicate over a short distance. In addition to the creation of a personal area network (PAN), Bluetooth also comes into play to enable communications for the IoT.
- **NFC:** Near field communication (NFC) is a set of communication protocols that enables two electronic devices to transfer information. Typically, one of these devices is a portable device such as a smartphone. NFC devices must be close to each other (within 4 cm, or 1.6 in). NFC devices are used in contactless payment systems, similar to those used in credit cards and electronic ticket smartcards, and allow mobile payment to replace/supplement these systems.
- **IR:** Infrared is another wireless technology that permits data transmission in short-range communication among computer peripherals and personal digital assistants. These devices usually conform to standards published by IrDA, the Infrared Data Association. Remote controls and IrDA devices use infrared light-emitting diodes (LEDs) to emit infrared radiation that is focused by a plastic lens into a narrow beam.
- **RFID:** Radio-frequency identification (RFID) uses electromagnetic fields to automatically identify and track tags attached to objects. The tags contain electronically stored information. Passive tags collect energy from a nearby RFID reader's interrogating radio waves. Active tags have a local power source such as a battery and may operate at hundreds of meters from the RFID reader. Unlike a barcode, the tag need not be within the line of sight of the reader, so it may be embedded in the tracked object.
- **802.11:** As detailed in Lesson 8, IEEE 802.11 is a set of Media Access Control and physical layer specifications for implementing wireless local area network (WLAN) computer communication in the 900MHz and 2.4GHz, 3.6GHz, 5GHz, and 60GHz frequency bands. Obviously, these technologies play a great role in the IoT because many appliances and common objects communicate over 802.11 wireless signals to reach a main hub. This is how most smart lights function, for example.

===============================================================

===============================================================

# 3.2 Network Infrastructure Devices
The devices used in a network infrastructure can vary based on the Layer 1 technology used. For example, a Token Ring network (which is rare today) might use a multistation access unit (MAU), whereas an Ethernet network might use a switch.  
  
Because Ethernet-based networks are dominant in today's LANs, however, the infrastructure devices presented here lend themselves to networks using Ethernet as the Layer 1 transport. Some devices (such as a router, for example) function basically the same regardless of the Layer 1 transport being used.

#### Hubs

As mentioned in Lesson 2, "The OSI Reference Model," a hub (specifically, an Ethernet hub in this discussion) lives at Layer 1 of the OSI model. As a result, a hub does not make forwarding decisions. Instead, a hub receives bits in on one port and then retransmits those bits out all other ports (that is, all ports on the hub other than the port on which the bits were received). This basic function of a hub has caused it to gain the nickname of a _bit spitter_.  
  
Hubs most often use UTP cabling to connect to other network devices; however, some early versions of Ethernet hubs (prior to the popularization of Ethernet switches) supported fiber-optic connections.  
  
The three basic types of Ethernet hubs are as follows:  

- **Passive hub:** Does not amplify (that is, electrically regenerate) received bits.
- **Active hub:** Regenerates incoming bits as they are sent out all the ports on a hub, other than the port on which the bits were received.
- **Smart hub:** The term _smart hub_ usually implies an active hub with enhanced features, such as Simple Network Management Protocol (SNMP) support.

A significant downside to hubs, and the main reason they have largely been replaced with switches, is that all ports on a hub belong to the same _collision domain_. As discussed in Lesson 4, a _collision domain_ represents an area on a LAN on which there can be only one transmission at a time. Because multiple devices can reside in the same collision domain, as is the case with multiple PCs connected to a hub, if two devices transmit at the same time, those transmissions _collide_ and have to be retransmitted.  
  
Because of the collision-domain issue, and the inefficient use of bandwidth (that is, bits being sent out all ports rather than only the port needing the bits), hubs are rarely seen in modern LANs. However, hubs are an important piece of the tapestry that makes up the history of Ethernet networks and represent characteristics found in different areas of modern Ethernet networks. For example, a wireless AP is much like a hub, in that all the wireless devices associated with the AP belong to the same collision domain.  
  
Consider Figure 3-14. Notice that the PCs depicted are interconnected using an Ethernet hub, but they are all in the same collision domain. As a result, only one of the connected PCs can transmit at any one time. This characteristic of hubs can limit scalability of hub-based LANs.  
  

![A figure shows an Ethernet hub at the center connected to four devices: a PC at the top, a printer on the right, a PC at the bottom, and a PC on the right. Text at the bottom reads "one collision domain and one broadcast domain".](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig14.jpg)

Figure 3-14: Ethernet Hub

  
Also notice that all devices on a hub belong to the same broadcast domain, which means that a broadcast sent into the hub will be propagated out all of the ports on the hub (other than the port on which the broadcast was received).

#### Bridges

A bridge joins two or more LAN segments, typically two Ethernet LAN segments. Each LAN segment is in separate collision domains, as shown in Figure 3-15. As a result, an Ethernet bridge can be used to scale Ethernet networks to a larger number of attached devices.  
  

![An illustration depicting the role of an Ethernet bridge is displayed along with the following components: file server, two Ethernet hubs, Ethernet bridge, and six PCs. The Ethernet bridge at the center is connected to two Ethernet hubs: one on the left and one on the right. Each hub is connected to two PCs at the top and to one PC at the bottom. The hub on the left is connected to a file server on its left. Text at the bottom reads, "Two Collision Domains and One Broadcast Domain."](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig15.jpg)

Figure 3-15: Ethernet Bridge

  
Unlike a hub, which blindly forwards received bits, a bridge (specifically, an Ethernet bridge in this discussion) makes intelligent forwarding decisions based on the destination MAC address present in a frame. Specifically, a bridge analyzes source MAC address information on frames entering the bridge and populates an internal MAC address table based on the learned information. Then, when a frame enters the bridge destined for a MAC address known by the bridge's MAC address table to reside off of a specific port, the bridge can intelligently forward the frame out the appropriate port. Because this operation is logically the same as switch operation, a more detailed description is presented in the upcoming discussion on switches. Because a bridge makes forwarding decisions based on Layer 2 information (that is, MAC addresses), a bridge is considered to be a Layer 2 device.  
  
Although a bridge segments a LAN into multiple collision domains (that is, one collision domain per bridge port), all ports on a bridge belong to the same broadcast domain. To understand this concept, think about the destination MAC address found in a broadcast frame. At Layer 2, the destination MAC address of a broadcast frame is FFFF.FFFF.FFFF in hexadecimal notation. Also, recall that a bridge filters frames (that is, sends frames only out necessary ports) if the bridge has previously learned the destination MAC address in its MAC address table. Because no device on a network will have a MAC address of FFFF.FFFF.FFFF, a bridge will never enter that MAC address in its MAC address table. As a result, broadcast frames are _flooded_ out all bridge ports other than the port that received the frame.  
  
Popular in the mid- to late 1980s and early 1990s, bridges have largely been replaced with switches, for reasons including price, performance, and features. From a performance perspective, a bridge makes its forwarding decisions in software, whereas a switch makes its forwarding decisions in hardware, using application-specific integrated circuits (ASICs). Also, not only do these ASICs help reduce the cost of switches, they enable switches to offer a wider array of features. For example, Lesson 4 discusses a variety of switch features, including VLANs, trunks, port mirroring, Power over Ethernet (PoE), and 802.1X authentication.

#### Switches

Like a bridge, a switch (specifically, a Layer 2 Ethernet switch in this discussion) can dynamically learn the MAC addresses attached to various ports by looking at the source MAC address on frames coming into a port. For example, if switch port Gigabit Ethernet 1/1 received a frame with a source MAC address of DDDD.DDDD. DDDD, the switch could conclude that MAC address DDDD.DDDD. DDDD resided off of port Gigabit Ethernet 1/1. In the future, if the switch receives a frame destined for a MAC address of DDDD.DDDD.DDDD, the switch would only send that frame out of port Gigabit Ethernet 1/1.  
  
Initially, however, a switch is unaware of what MAC addresses reside off of which ports (unless MAC addresses have been statically configured). Therefore, when a switch receives a frame destined for a MAC address not yet present in the switch's MAC address table, the switch floods that frame out of all the switch ports except the port on which the frame was received. Similarly, broadcast frames (that is, frames with a destination MAC address of FFFF.FFFF.FFFF) are always flooded out all switch ports except the port on which the frame was received. As mentioned in the discussion on bridges, the reason broadcast frames are always flooded is that no endpoint will have a MAC address of FFFF.FFFF.FFFF, meaning that the FFFF.FFFF.FFFF MAC address will never be learned in a switch's MAC address table.  
  
To illustrate how a switch's MAC address table becomes populated, consider an endpoint named PC1 that wants to form a Telnet connection with a server. Also, assume that PC1 and its server both reside on the same subnet (that is, no routing is required to get traffic between PC1 and its server). Before PC1 can send a Telnet session to its server, PC1 needs to know the IP address (that is, the Layer 3 address) and the MAC address (Layer 2 address) of the server. The IP address of the server is typically known or is resolved via a Domain Name System (DNS) lookup. In this example, assume the server's IP address is known. To properly form a Telnet segment, however, PC1 needs to know the server's Layer 2 MAC address. If PC1 does not already have the server's MAC address in its ARP cache, PC1 can send an Address Resolution Protocol (ARP) request in an attempt to learn the server's MAC address, as shown in Figure 3-16.  
  

![A figure shows an ARP request from a PC to a server. The figure shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP request is sent from PC to SW1. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column headers read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and empty. Row 2 reads, Gig 0/2 and empty. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and empty. Row 2 reads, Gig 0/2 and empty.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig16.jpg)

Figure 3-16: Endpoint Sending an ARP Request

  
When switch SW1 sees PC1's ARP request enter port Gigabit 0/1, PC1's MAC address of AAAA.AAAA.AAAA is added to switch SW1's MAC address table. Also, because the ARP request is a broadcast, its destination MAC address is FFFF.FFFF.FFFF. Because the MAC address of FFFF.FFFF.FFFF is not known to switch SW1's MAC address table, switch SW1 floods a copy of the incoming frame out all switch ports, other than the port on which the frame was received, as shown in Figure 3-17.  
  

![An illustration shows the flooding of an ARP request by switch, SW1. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP request is sent from PC to PC2, PC3, and SW2 via SW1. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column headers read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and empty. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and empty. Row 2 reads, Gig 0/2 and empty.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig17.jpg)

Figure 3-17: Switch SW1 Flooding the ARP Request

  
When switch SW2 receives the ARP request over its Gig 0/1 trunk port, the source MAC address of AAAA.AAAA.AAAA is added to switch SW2's MAC address table, as illustrated in Figure 3-18. Also, similar to the behavior of switch SW1, switch SW2 floods the broadcast.  
  

![An illustration shows the flooding of an ARP request by switch SW2. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP request is sent from PC to PC2, PC3, and SW2 via SW1. The ARP request from SW2 goes to PC4, PC5, and server. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column heads read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, AAAA.AAAA.AAAA and empty. Row 2 reads, Gig 0/2 and empty. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and empty.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig18.jpg)

Figure 3-18: Switch SW2 Flooding the ARP Request

  
The server receives the ARP request and responds with an ARP reply, as shown in Figure 3-19. Unlike the ARP request, however, the ARP reply frame is not a broadcast frame. The ARP reply, in this example, has a destination MAC address of AAAA.AAAA.AAAA. This makes the ARP reply a unicast frame.  
  

![An illustration shows an ARP reply from the server. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP reply is sent from the server to SW2. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column headers read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and empty. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and empty.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig19.jpg)

Figure 3-19: ARP Reply Sent from the Server

  
Upon receiving the ARP reply from the server, switch SW2 adds the server's MAC address of BBBB.BBBB.BBBB to its MAC address table, as shown in Figure 3-20. Also, the ARP reply is only sent out port Gig 0/1 because switch SW2 knows that the destination MAC address of AAAA.AAAA.AAAA is available off of port Gig 0/1.  
  

![An illustration shows the forwarding of an ARP reply by switch, SW2. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP reply is sent from the server to SW1 via SW2. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column headers read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and empty. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig20.jpg)

Figure 3-20: Switch SW2 Forwarding the ARP Reply

  
When receiving the ARP reply in its Gig 0/2 port, switch SW1 adds the server's MAC address of BBBB.BBBB.BBBB to its MAC address table. Also, like switch SW2, switch SW1 now has an entry in its MAC address table for the frame's destination MAC address of AAAA.AAAA.AAAA. Therefore, switch SW1 forwards the ARP reply out port Gig 0/1 to the endpoint of PC1, as illustrated in Figure 3-21.  
  

![An illustration shows the forwarding of an ARP reply by switch, SW1. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. An ARP reply is sent from the server to SW1 via SW2. From SW2, the ARP reply is forwarded to PC1. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column heads read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig21.jpg)

Figure 3-21: Switch SW1 Forwarding the ARP Reply

  
After receiving the server's ARP reply, PC1 now knows the MAC address of the server. Therefore, PC1 can now properly construct a Telnet segment destined for the server, as depicted in Figure 3-22.  
  

![An illustration shows a TELNET segment sent by a PC. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. PC1 sends a TELNET segment to SW1. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column heads read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig22.jpg)

Figure 3-22: PC1 Sending a Telnet Segment

  
Switch SW1 has the server's MAC address of BBBB.BBBB.BBBB in its MAC address table. Therefore, when switch SW1 receives the Telnet segment from PC1, that segment is forwarded out of switch SW1's Gig 0/2 port, as shown in Figure 3-23.  
  

![An illustration shows the forwarding of a TELNET segment by switch, SW1. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. PC1 sends a TELNET segment to SW1. The TELNET segment is forwarded to SW2 by SW1. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column heads read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig23.jpg)

Figure 3-23: Switch SW1 Forwarding the Telnet Segment

  
Similar to the behavior of switch SW1, switch SW2 forwards the Telnet segment out of its Gig 0/2 port. This forwarding, shown in Figure 3-24, is possible, because switch SW2 has an entry for the segment's destination MAC address of BBBB.BBBB.BBBB in its MAC address table.  
  

![An illustration shows the forwarding of a TELNET segment by switch, SW2. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and a server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. The TELNET segment from PC1 reaches the server via SW1 and SW2. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column heads read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig24.jpg)

Figure 3-24: Switch SW2 Forwarding the Telnet Segment

  
Finally, the server responds to PC1, and a bidirectional Telnet session is established between PC1 and the server, as illustrated in Figure 3-25. Because PC1 learned the server's MAC address as a result of its earlier ARP request and stored that result in its local ARP cache, the transmission of subsequent Telnet segments does not require additional ARP requests. However, if unused for a period of time, entries in a PC's ARP cache can time out. Therefore, the PC would have to broadcast another ARP frame if it needed to send traffic to the same destination IP address. The sending of the additional ARP adds a small amount of delay when reestablishing a session with that destination IP address.  
  

![An illustration shows the establishment of TELNET session between a server and a PC. The illustration shows the following components: two switches labeled SW1 and SW2, five PCs labeled PC1, PC2, PC3, PC4, and PC5, and server. Port Gig 0/1 of SW1 is connected to PC1 of MAC address AAAA.AAAA.AAAA. Port Gig 0/2 of SW1 is connected to port Gig 0/1 of SW2. Port Gig 0/3 of SW1 is connected to PC2. Port Gig 0/4 of SW1 is connected to PC3. Port Gig 0/2 of SW2 is connected to the server with MAC address BBBB.BBBB.BBBB. Port Gig 0/3 of SW2 is connected to PC4. Port Gig 0/4 of SW2 is connected to PC5. A TELNET session is established between PC1 and server via SW1 and SW2. Below the network are MAC Address tables for SW1 and SW2 with two rows and two columns. Column headers read, Port and MAC Addresses. SW1 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB. SW2 MAC Address table shows the following: Row 1 reads, Gig 0/1 and AAAA.AAAA.AAAA. Row 2 reads, Gig 0/2 and BBBB.BBBB.BBBB.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig25.jpg)

Figure 3-25: Bidirectional Telnet Session Between PC1 and the Server

  
As shown in Figure 3-26, like on a bridge, each port on a switch represents a separate collision domain. Also, all ports on a switch belong to the same broadcast domain, with one exception.  
  

![A figure shows a layer 2 switch at the center connected to four devices: a PC at the top, a file server on the left, a PC at the bottom, and a printer at the bottom-right. Text at the bottom reads "four collision domains and one broadcast domain".](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig26.jpg)

Figure 3-26: Switch Collision and Broadcast Domains

  
The exception is when the ports on a switch have been divided up into separate virtual LANs (VLANs). As discussed in Lesson 5, "IPv4 and IPv6 Addresses," each VLAN represents a separate broadcast domain, and for traffic to travel from one VLAN to another, that traffic must be routed by a Layer 3 device.

#### Multilayer Switches

Whereas a Layer 2 switch, as previously described, makes forwarding decisions based on MAC address information, a multilayer switch can make forwarding decisions based on upper-layer information. For example, a multilayer switch could function as a router and make forwarding decisions based on destination IP address information.  
  
Some literature refers to a multilayer switch as a _Layer 3 switch_ because of the switch's capability to make forwarding decisions like a router. The term _multilayer switch_ is more accurate, however, because many multilayer switches have policy-based routing features that allow upper-layer information (for example, application port numbers) to be used in making forwarding decisions.  
  
Figure 3-27 makes the point that a multilayer switch can be used to interconnect not just network segments, but entire networks. Specifically, Lesson 6, "Routing IP Packets," explains how logical Layer 3 IP addresses are used to assign network devices to different logical networks. For traffic to travel between two networked devices that belong to different networks, that traffic must be _routed_. (That is, a device, such as a multilayer switch, has to make a forwarding decision based on Layer 3 information.)  
  

![A figure depicts the role of a multilayer switch. The components are as follows: multilayer switch, two layer 2 switches, printer, file server, and four PCs. The multilayer switch at the center is connected to layer 2 switch on the left and the right. The switch on the left is connected to three devices: a PC at the top, a file server on the left, and a PC at the bottom. The switch on the right is connected to three devices: a PC at the top, a printer on the left, and a PC at the bottom. The region to the left and right of the multilayer switch is marked as network A and network B, respectively.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig27.jpg)

Figure 3-27: Multilayer Ethernet Switch

  
Like on a Layer 2 switch, each port on a multilayer switch represents a separate collision domain; however, a characteristic of a multilayer switch (and a router) is that it can become a boundary of a broadcast domain. Although all ports on a Layer 2 switch belong to the same broadcast domain, if configured as such, all ports on a multilayer switch can belong to different broadcast domains.

#### Routers

A router is a Layer 3 device, meaning that it makes forwarding decisions based on logical network address (for example, IP address) information. Although a router is considered to be a Layer 3 device, like a multilayer switch, it has the capability to consider high-layer traffic parameters, such as quality of service (QoS) settings, in making its forwarding decisions.  
  
As shown in Figure 3-28, each port on a router is a separate collision domain and a separate broadcast domain. At this point in the discussion, routers are beginning to sound much like multilayer switches. So, why would network designers select a router rather than a multilayer switch in their design?  
  

![An illustration depicts the various domains of a router. The router at the center is connected to a switch on either side. The region to the left and right of the router is marked network A and network B, respectively. The switch on the left is connected to three devices: a PC at the top, a file server on the left, and a PC at the bottom. The switch on the right is connected to three devices: a PC at the top, a printer on the right, and a PC at the bottom. Text at the bottom reads "eight collision domains and two broadcast domain".](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig28.jpg)

Figure 3-28: Router Broadcast and Collision Domains
  
One reason a router is preferable to a multilayer switch, in some cases, is that routers are usually more feature rich and support a broader range of interface types. For example, if you need to connect a Layer 3 device out to your Internet service provider (ISP) using a serial port, you will be more likely to find a serial port expansion module for your router rather than your multilayer switch

![[Pasted image 20230618002010.png]]


![[Pasted image 20230618002142.png]]

===============================================================

# 3.3 Specialized Network Devices
Although network infrastructure devices make up the backbone of a network, for added end-user functionality, many networks integrate various specialized network devices such as VPN concentrators, firewalls, DNS servers, DHCP servers, proxy servers, caching engines, and content switches.

#### VPN Concentrators

Companies with locations spread across multiple sites often require secure communications between those sites. One option is to purchase multiple WAN connections interconnecting those sites. Sometimes, however, a more cost-effective option is to create secure connections through an untrusted network, such as the Internet. Such a secure tunnel is called a _virtual private network_ (VPN). Depending on the VPN technology being used, the devices that terminate the ends of a VPN tunnel might be required to perform heavy processing. For example, consider a company headquarters location with VPN connections to each of 100 remote sites. The device at the headquarters terminating these VPN tunnels might have to perform encryption and authentication for each tunnel, resulting in a heavy processor burden on that device.  
  
Although several router models can terminate a VPN circuit, a dedicated device, called a _VPN concentrator_, can be used instead. A VPN concentrator performs the processor-intensive process required to terminate multiple VPN tunnels. Figure 3-29 shows a sample VPN topology, with a VPN concentrator at each corporate location.  
  

![A figure illustrates the role of a VPN Concentrator. The figure shows an internet cloud at the center surrounded by three buildings (at the top, right, and bottom) labeled branch A, branch B, and branch C. To the left of the cloud, a headquarters is shown. Each building and headquarters has a VPN Concentrator. The headquarters is connected to branch A, branch B, and branch C via internet cloud.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig29.jpg)

Figure 3-29: VPN Concentrator

  
The term _encryption_ refers to the capability of a device to scramble data from a sender in such a way that the data can be unscrambled by the receiver, but not by any other party who might intercept the data. With a VPN concentrator's capability to encrypt data, it is considered to belong to a class of devices called _encryption devices_, which are devices (for example, routers, firewalls, and VPN concentrators) capable of participating in an encrypted session.

#### Firewalls

A firewall is primarily a network security appliance, and it is discussed in Lesson 12, "Network Security." As depicted in Figure 3-30, a firewall stands guard at the door of your network, protecting it from malicious Internet traffic.  
  

![Two figures at the top and bottom depict the role of a firewall. The figure at the top and bottom shows the following components connected horizontally using Ethernet cable: PC, switch, router, and firewall. The firewall is connected to internet cloud via serial cable. The figure at the top shows a rightward arrow labeled "initial request" pointing from PC to internet and a leftward arrow labeled "reply" pointing to PC from the internet. The figure at the bottom shows a rightward arrow labeled "initial request" pointing to the firewall from the internet. A starburst above the firewall reads, block.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig30.jpg)

Figure 3-30: Firewall

  
For example, a _stateful firewall_ allows traffic to originate from an inside network (that is, a trusted network) and go out to the Internet (an untrusted network). Likewise, return traffic coming back from the Internet to the inside network is allowed by the firewall. However, if traffic were originated from a device on the Internet (that is, not returning traffic), the firewall blocks that traffic.

#### DNS Servers

A Domain Name System (DNS) server performs the task of taking a domain name (for example, [www.ciscopress.com](http://www.ciscopress.com/)) and resolving that name into a corresponding IP address (for example, 10.1.2.3). Because routers (or multilayer switches) make their forwarding decisions based on Layer 3 information (for example, IP addresses), an IP packet needs to contain IP address information, not DNS names. However, as humans, we more readily recall meaningful names rather than 32-bit numbers.  
  
As shown in Figure 3-31, an end user who wants to navigate to the [www.ciscopress.com](http://www.ciscopress.com/) website enters that fully qualified domain name (FQDN) into her web browser; however, the browser cannot immediately send a packet destined for [www.ciscopress.com](http://www.ciscopress.com/). First, the end user's computer needs to take the FQDN of [www.ciscopress.com](http://www.ciscopress.com/) and resolve it into a corresponding IP address, which can be inserted as the destination IP address in an IP packet. This resolution is made possible by a DNS server, which maintains a database of local FQDNs and their corresponding IP addresses, in addition to pointers to other servers that can resolve IP addresses for other domains.  
  

![A figure depicts the role of a DNS server. The figure shows the following components connected horizontally using Ethernet cable: PC, switch, and router. The router is connected to an internet cloud via serial cable. The switch is connected to a DNS server at the top. An arrow labeled "(1) What is the IP address for www.ciscopress.com?" points to DNS server from PC. An arrow labeled "(2) 192.168.1.11" points to PC from DNS server. An arrow labeled "(3) packet destined for 192.168.1.11" points to the internet cloud from PC via switch and router.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig31.jpg)

Figure 3-31: DNS Server

  
A FQDN is a series of strings, delimited by a period (as in the example, [www.ciscopress.com](http://www.ciscopress.com/)). The rightmost part is the top-level domain. Examples of top-level domains include .com, .mil, and .edu, as shown in Figure 3-32. Although there are many other top-level domains, these are among some of the more common top-level domains seen in the United States.  
  

![A diagram illustrates the hierarchy of the Domain Name Structure. <BR>The diagram shows a node at the top labeled root that has three branch nodes: .com, .mil, and .edu. The .com node, in turn, has three sub-nodes: Cisco, Amazon, and Twitter. The .mil node, in turn, has three sub-nodes: USCG, af, and army. The .edu node, in turn, has three sub-nodes: eku, Purdue, and yale. The Purdue node is further classified into two: cs and science.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig32.jpg)

Figure 3-32: Hierarchical Domain Name Structure

  
Lower-level domains can point upward to higher-level DNS servers to resolve nonlocal FQDNs, as illustrated in Figure 3-32.  
  
A DNS server's database contains not only FQDNs and corresponding IP addresses, but also DNS record types. For example, a Mail Exchange (MX) record would be the record type for an email server. As a few examples, Table 3-2 lists a collection of common DNS record types.

![[Pasted image 20230620235919.png]]

A potential challenge when setting up DNS records is when you want to point to the IP address of a device that might change its IP address. For example, if you have a cable modem or digital subscriber line (DSL) modem in your home, that device might obtain its IP address from your service provider via DHCP (as discussed in the next section, "DHCP Servers"). As a result, if you add the IP address of your cable modem or DSL modem to a DNS record (to allow users on the Internet to access one or more devices inside your network), that record could be incorrect if your device obtains a new IP address from your service provider.  
  
To overcome such a challenge, you can turn to dynamic DNS (DDNS). A DDNS provider supplies software you run on one of your PCs that monitors the IP address of the device referenced in the DNS record (your cable modem or DSL modem in this example). If the software detects a change in the monitored IP address, that change is reported to your service provider, which is also providing DNS service.  
  
Another option is IP address management (IPAM). This is a means of planning, tracking, and managing the Internet Protocol address space used in a network. IPAM integrates DNS and DHCP so that each is aware of changes in the other (for instance DNS knowing of the IP address taken by a client via DHCP, and updating itself accordingly).  
  
Yet another DNS variant is Extension Mechanisms for DNS (EDNS). The original specification for DNS had size limitations that prevented the addition of certain features, such as security. EDNS supports these additional features, while maintaining backward compatibility with the original DNS implementation. Rather than using new flags in the DNS header, which would negate backwards compatibility, EDNS sends optional pseudo-resource-records between devices supporting EDNS. These records support 16 new DNS flags. If a legacy DNS server were to receive one of these optional records, the record would simply be ignored. Therefore, backward compatibility is maintained, while new features can be added for newer DNS servers.  
  
When you enter a web address into your browser in the form of http://_FQDN_ (for example, [http://www.ajsnetworking.com](http://www.ajsnetworking.com/)), notice that you not only indicate the FQDN of your web address, you also specify that you want to access this location using the HTTP protocol. Such a string, which indicates both an address (for example, [www.ajsnetworking.com](http://www.ajsnetworking.com/)) and a method for accessing that address (for example, http://), is called a _uniform resource locator_ (URL).  
  
Organizations will often implement DNS name resolution using internal and external DNS. This means that clients using DNS to resolve for internal resources will rely on a DNS server installed within the organization, while clients needing to resolve external resources will rely on the Internet (external) DNS servers. You can take steps to ensure the internal use only DNS information is not shared with public, external DNS servers.  
  
Another option often used today for implementing DNS is third-party or cloud-hosted DNS. Amazon Web Services, for example, offers their Route 53 service. This powerful set of DNS services permits everything from domain registrations to name resolution services for your cloud or on-prem servers and clients.

#### DHCP Servers

Most modern networks have IP addresses assigned to network devices, and those logical Layer 3 addresses are used to route traffic between different networks. However, how does a network device receive its initial IP address assignment?  
  
One option is to manually configure an IP address on a device; however, such a process is time consuming and error prone. A far more efficient method of IP address assignment is to dynamically assign IP addresses to network devices. The most common approach for this auto-assignment of IP addresses is Dynamic Host Configuration Protocol (DHCP). Not only does DHCP assign an IP address to a network device, it can assign a wide variety of other IP parameters, such as a subnet mask, a default gateway, and the IP address of a DNS server.  
  
If you have a cable modem or DSL connection in your home, your cable modem or DSL router might obtain its IP address from your service provider via DHCP. In many corporate networks, when a PC boots, that PC receives its IP address configuration information from a corporate DHCP server.  
  
Figure 3-33 illustrates the exchange of messages that occur as a DHCP client obtains IP address information from a DHCP server. The following list describes each step in further detail:  
  

![A figure shows the exchange of messages between a DHCP client and a DHCP server. The DHCP client on the left is connected to the DHCP server of IP address 10.1.1.2 via Ethernet cable. In step 1, an arrow labeled DHCPDISCOVER from client points to the server. In step 2, an arrow labeled DHCPOFFER from server points to the client. In step 3, an arrow labeled DHCPREQUEST from client points to the server. In step 4, an arrow labeled DHCPACK from server points to the client.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig33.jpg)

Figure 3-33: Obtaining IP Address Information from a DHCP Server

1. When a DHCP client initially boots, it has no IP address, default gateway, or other such configuration information. Therefore, the way a DHCP client initially communicates is by sending a broadcast message (that is, a DHCPDISCOVER message to a destination address of 255.255.255.255) in an attempt to discover a DHCP server.
2. When a DHCP server receives a DHCPDISCOVER message, it can respond with a unicast DHCPOFFER message. Because the DHCPDISCOVER message is sent as a broadcast, more than one DHCP server might respond to this discover request. However, the client typically selects the server that sent the first DHCPOFFER response received by the client.
3. The DHCP client communicates with this selected server by sending a unicast DHCPREQUEST message asking the DHCP server to provide IP configuration parameters.
4. The DHCP server responds to the client with a unicast DHCPACK message. This DHCPACK message contains a collection of IP configuration parameters.

Notice that in step 1, the DHCPDISCOVER message was sent as a broadcast. By default, a broadcast cannot cross a router boundary. Therefore, if a client resides on a different network than the DHCP server, the client's next-hop router should be configured as a DHCP relay agent, which allows a router to relay DHCP requests to either a unicast IP address or a directed broadcast address for a network. The DHCP relay agent is often referred to as an _IP helper_.  
  
A DHCP server can be configured to assign IP addresses to devices belonging to different subnets. Specifically, the DHCP server can determine the source subnet of the DHCP request and select an appropriate address pool from which to assign an address. One of these address pools (which typically corresponds to a single subnet) is called a _scope_.  
  
When a network device is assigned an IP address from an appropriate DHCP scope, that assignment is not permanent. Rather, it is a temporary assignment referred to as a _lease_. Although most client devices on a network work well with this dynamic addressing, some devices (for example, servers) might need to be assigned a specific IP address. Fortunately, you can configure a DHCP reservation, where a specific MAC address is mapped to a specific IP address, which will not be assigned to any other network device. This static addressing approach is referred to as a DHCP _reservation_.  
  
Another common concern in DHCP configurations is to exclude IP addresses from the scope of addresses you make available. We call these IP exclusions. You might do this for several servers you have in your organization that required configurations with a static IP address in the scope of your overall IP address space. IP exclusions are simple to configure and ensure that an IP address conflict does not result in your subnet.  
  
A method for remembering the four main steps of DHCP is D.O.R.A., with each letter representing the steps discover, offer, request, and acknowledge.

#### Proxy Servers

Some clients are configured to forward their packets, which are seemingly destined for the Internet, to a proxy server. This proxy server receives the client's request, and on behalf of that client (that is, as that client's proxy), the proxy server sends the request out to the Internet. When a reply is received from the Internet, the proxy server forwards the response on to the client. Figure 3-34 illustrates the operation of a proxy server.  
  

![A figure illustrates the operation of a Proxy server. The figure shows the following component connected horizontally using Ethernet cable: PC, switch, and router. The router is connected to an internet cloud via serial cable. The switch is connected to a Proxy server at the top. A request from PC goes to the proxy server. The request is forwarded from proxy to the internet cloud via the router. A reply from the internet cloud goes to the proxy server via the router. The reply is forwarded from the proxy to the PC.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig34.jpg)

Figure 3-34: Proxy Server Operation

  
What possible benefit could come from such an arrangement? Security is one benefit. Specifically, because all requests going out to the Internet are sourced from the proxy server, the IP addresses of network devices inside the trusted network are hidden from the Internet.  
  
Yet another benefit could come in the form of bandwidth savings, because many proxy servers perform content caching. For example, without a proxy server, if multiple clients all visited the same website, the same graphics from the home page of the website would be downloaded multiple times (one time for each client visiting the website). However, with a proxy server performing content caching, when the first client navigates to a website on the Internet, and the Internet-based web server returns its content, the proxy server not only forwards this content to the client requesting the web page but stores a copy of the content on its hard drive. Then, when a subsequent client points its web browser to the same website, after the proxy server determines that the page has not changed, the proxy server can locally serve up the content to the client, without having to once again consume Internet bandwidth to download all the graphic elements from the Internet-based website.  
  
As a final example of a proxy server benefit, some proxy servers can perform content filtering. Content filtering restricts clients from accessing certain URLs. For example, many companies use content filtering to prevent their employees from accessing popular social networking sites, in an attempt to prevent a loss of productivity. A reverse proxy receives requests on behalf of a server or servers and replies back to the clients on behalf of those servers. This can also be used with load-balancing and caching to better utilize a group of servers.

#### Content Engines

As previously described, many proxy servers are capable of performing content caching; however, some networks used dedicated appliances to perform this content caching. These appliances are commonly referred to as _caching engines_ or _content engines_.  
  
Figure 3-35 demonstrates how a corporate branch office can locally cache information from a server located at the corporate headquarters location. Multiple requests from branch office clients for the content can then be serviced from the content engine at the branch office, thus eliminating the repetitive transfer of the same data. Depending on traffic patterns, such an arrangement might provide significant WAN bandwidth savings.  
  

![A figure illustrates the operation of a content engine. The figure shows a branch office on the left and a headquarters (HQ) on the right. The branch office shows the following connections: switch at the center is connected to three devices: a PC at the top, a content engine at the bottom, and a router on the right. The headquarters shows the following connections: switch at the center is connected to two devices: a router on the left and a file server at the bottom. The router in the branch office and in the headquarters are connected to IP WAN cloud via serial cable. A request from PC is sent to the content engine via a switch. A reply from the content engine goes to the PC via a switch. An arrow labeled "content from the HQ Server Is Sent to the Branch Office Content Engine" from server goes to the content engine.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig35.jpg)

Figure 3-35: Content Engine Operation

#### Content Switches

Consider the server farm presented in Figure 3-36. The servers making up this server farm house the same data. For companies with a large Internet presence (for example, a search engine company, an online book store, or a social networking site), a single server could be overwhelmed with the glut of requests flooding in from the Internet. To alleviate the burden placed on a single server, a content switch (also known as a _load balancer_) distributes incoming requests across the various servers in the server farm, each of which maintains an identical copy of data and applications.  
  

![A figure illustrates the operation of a content switch. The figure shows an internet cloud connected to a router via serial cable. A section labeled "server farm" has a content switch that is connected to five servers: one at the top, one at the bottom, and three on the right. The router, in turn, is connected to the content switch of the server farm on its right.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig36.jpg)

Figure 3-36: Content Switching Operation

  
A major benefit of content switching is that it allows a server farm to scale. Specifically, as demand increases, new servers can be added to the group of servers across which requests are load balanced. Also, if maintenance (for example, applying an operating system patch) needs to be performed on a server, a server can simply be taken out of the load-balancing rotation, with the remaining servers picking up the slack. Then, after the maintenance is complete, the server can once again be added back to the defined server group.

#### Other Specialized Devices

Here are some other specialized networking devices not explicitly covered elsewhere in this text:  

- **Wireless range extender:** Since all 802.11 wireless technologies have distance limitations, a wireless range extender can amplify the signal and extend the reachability of a wireless cell.
- **Next-generation firewall (NGFW):** Newer firewalls of today not only can perform stateless and stateful filtering of traffic, but they can also deeply inspect the contents of packets to find and prevent attacks. These devices also can connect to the cloud for the latest updates in global threats.
- **Software-defined networking (SDN) controller:** This appliance-based device is responsible for distributing control plane instructions to network devices downstream for their configuration and management. If you are not familiar with SDN, have no fear: the next section of this lesson explains it to you.

![[Pasted image 20230620133823.png]]

![[Pasted image 20230620134452.png]]

===============================================================

# 3.4 Virtual Network Devices
#### Virtual Servers

The computing power available in a single high-end server is often sufficient to handle the tasks of multiple independent servers. With the advent of virtualization, multiple servers (which might be running different operating systems) can run in virtual server instances on one physical device. For example, a single high-end server might be running an instance of a Microsoft Windows Server providing Microsoft Active Directory (AD) services to an enterprise, while simultaneously running an instance of a Linux server acting as a corporate web server, and at the same time acting as a Sun Solaris UNIX server providing corporate DNS services. Figure 3-37 illustrates this concept of a virtual server. Although the virtual server in the figure uses a single network interface card (NIC) to connect out to an Ethernet switch, many virtual server platforms support multiple NICs. Having multiple NICs offers increased throughput and load balancing.  
  

![A figure illustrates the concept of a virtual server. The figure shows a virtual server connected to an Ethernet switch through a single NIC. The virtual server shows three segments. The first segment contains Microsoft Windows Active Directory and Linux Web Server. The third segment contains Sun Solaris DNS Server.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig37.jpg)

Figure 3-37: Virtual Server

  

Note

Although the previous example used a Linux-based web server, be aware that web servers can run on a variety of operating system (OS) platforms. As one example, Microsoft Windows servers support a web server application called _Internet Information Services_ (IIS), which was previously known as Internet Information Server.

  
Virtualization is possible with servers thanks to specialized software called a _hypervisor_. The hypervisor takes physical hardware and abstracts it for the virtual server. The extent of virtualization is amazing, with even the NIC of each virtual server represented virtually (virtual NIC).  
  
The networks and systems supporting virtual servers also commonly have network-attached storage (NAS), where disk storage is delivered as a service over the network. A technology for network storage is IP-based Small Computer System Interface (iSCSI). With iSCSI, a client using the storage is referred to as an _initiator_, and the system providing the iSCSI storage is called the iSCSI _target_. The networks supporting iSCSI are often configured to support larger-than-normal frame sizes, referred to as _jumbo frames_.  
  
Fibre channel is another technology that can deliver storage services over a network. Thanks to high-speed Ethernet options today, you can even configure Fibre Channel over Ethernet (FCoE) to run a unified network for your SAN and non-storage-data traffic.  
  

Note

Less commonly encountered is InfiniBand (IB). This communication technology permits high-speed, low-latency communications between supercomputers.

#### Virtual Routers and Firewalls

Most of the vendors who create physical routers and firewalls also have an offering that includes virtualized routers and firewalls. The benefit of using a virtualized firewall or router is that the same features of routing and security can be available in the virtual environment as they are in the physical environment. As part of interfacing with virtual networks, virtual network adapters can be used. For connectivity between the virtual world and the physical one, there would be physical interfaces involved that connect to the logical virtual interfaces.

#### Virtual Switches

One potential trade-off you make with the previously described virtual server scenario is that all servers belong to the same IP subnet, which could have QoS and security implications. If these server instances ran on separate physical devices, they could be attached to different ports on an Ethernet switch. These switch ports could belong to different VLANs, which could place each server in a different broadcast domain.  
  
Fortunately, some virtual servers allow you to still have Layer 2 control (for example, VLAN separation and filtering). This Layer 2 control is made possible by the virtual server not only virtualizing instances of servers, but also virtualizing a Layer 2 switch. Figure 3-38 depicts a virtual switch. Notice that the servers logically reside on separate VLANs, and frames from those servers are appropriately tagged when traveling over a trunk to the attached Ethernet switch.  
  

![A figure illustrates the concept of a virtual switch. The figure shows a virtual server connected to an Ethernet switch through a single NIC. The virtual server shows three segments. The first segment contains Microsoft Windows Active Directory and Linux Web Server. The second segment has a virtual switch. The third segment contains Sun Solaris DNS Server. The virtual switch is connected Microsoft Windows Active Directory via VLAN 10. The virtual switch is connected to Linux Web Server via VLAN 20. The virtual switch is connected to Sun Solaris DNS Server via VLAN 30. The connection between the virtual server and the Ethernet switch is labeled trunk.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig38.jpg)

Figure 3-38: Virtual Server with a Virtual Switch

#### Virtual Desktops

Another emerging virtualization technology is virtual desktops. With today's users being more mobile than ever, they need access to information traditionally stored on their office computers' hard drives from a variety of other locations. For example, a user might be at an airport using their smartphone, and they need access to a document they created on their office computer. With virtual desktops, a user's data is stored in a data center rather than on an office computer's hard drive. By providing authentication credentials, the user can establish a secure connection between the centralized repository of user data and their device, as shown in Figure 3-39, thus allowing the user to remotely access the desired document.  
  

![An illustration depicts the concept of a virtual desktop. The illustration shows two buildings: one on the left and one on the right. The building on the left shows the following connections: a switch at the center is connected to three devices: a remote desktop server at the top, a user's office computer on the left, and a router on the right. The building on the right shows the following connections: a switch at the center is connected to two devices: a router on the left and a mobile user at the top. The routers on the buildings are connected to an IP WAN cloud via serial cable.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig39.jpg)

Figure 3-39: Virtual Desktop Topology

#### Other Virtualization Solutions

Although the previously discussed virtualization technologies (that is, virtual servers, virtual switches, and virtual desktops) were described as residing at a corporate location (that is, _on-site_), some service providers offer _off-site_ options. Specifically, if a service provider's customer did not want to house and maintain its own data center, these virtualization technologies could be located at a service provider's data center, and the customer could be billed based on usage patterns. Such a service provider offering is called _network as a service_ (NaaS), implying that network features can be provided by a service provider, just as a telephony service provider offers access to the Public Switched Telephone Network (PSTN), and an ISP offers access to the public Internet.

#### Cloud Computing

Virtualized services and solutions are often offered by service providers as _cloud computing_. A company purchasing cloud computing services has the option of public, private, or hybrid cloud services. Private cloud services include systems that only have interactions and communications with other devices inside that same private cloud or system. Public cloud services interact with devices on public networks such as the Internet and potentially other public clouds. An environment in which there are private cloud services, but some of those services interact with public clouds, is referred to as _hybrid cloud services_. Some of the types of services that can be available as part of cloud computing include _infrastructure as a service_ (IaaS), where the company rents virtualized servers (which are hosted by a service provider) and then runs specific applications on those servers. Another type of cloud service is _software as a service_ (SaaS), where the details of the servers are hidden from the customer and the customer's experience is similar to using a web-based application. Another cloud service is called _platform as a service_ (PaaS), which can provide a development platform for companies that are developing applications and want to focus on creating the software and not have to worry about the servers and infrastructure that are being used for that development. Another type of cloud is the _community cloud_, which is a term referring to cloud services used by individuals, companies, or entities with similar interests. In cloud computing, it is likely that virtualized switches, routers, servers, and firewalls will be used as part of cloud-based services.  
  

Note

An application service provider (ASP) provides application software access to subscribers. This service is sometimes called _software as a service_ (SaaS).

  
Similar to outsourcing the features of a data network with NaaS, a corporate telephony solution might also be outsourced. Many companies own and maintain their own private branch exchange (PBX), which is a privately owned telephone system. One option for companies that want to outsource their telephony service is to use a service provider's virtual PBX. A virtual PBX is usually a Voice over IP (VoIP) solution, where voice is encapsulated inside data packets for transmission across a data network. Typically, a service provider provides all necessary IP telephony gateways to convert between a customer's existing telephony system and the service provider's virtual PBX.  
  

Note

A virtual PBX is different from a hosted PBX, which is usually a traditional (that is, not VoIP) PBX hosted by a service provider.

  
As more and more technology appears in the cloud (either public or private), connectivity (specifically, secured connectivity) becomes paramount. Secure protocols such as HTTPS, TLS, and SSH are a must when accessing most cloud resources. Fortunately, massive cloud providers such as Amazon with Amazon Web Services (AWS) make it simple to securely connect using a wide variety of methods, including hardware VPN appliances located at your corporate or home office. Although your applications and servers might be sharing physical equipment with other customers of Amazon, great pains are taken to ensure this multitenancy does not sacrifice security.  
  

Note

Amazon makes it very clear. When it comes to your cloud security with Amazon Web Services, it is a shared responsibility model. For example, Amazon will secure your virtual machine from other customer virtual machines, but it is up to you to properly secure the operating system (OS) inside the VM, just as it is your responsibility to control access to and from the VM.

#### Software-Defined Networking (SDN)

Software-defined networking is changing the landscape of our traditional networks. A well-implemented software-defined network will allow the administrator to implement features, functions, and configurations without the need to do the individual command-line configuration on the network devices. The front end that the administrator interfaces with can alert the administrator to what the network is currently doing, and then through that same graphical user interface the administrator can indicate what he wants done, and then behind the scenes the detailed configurations across multiple network devices can be implemented by the software-defined network.

===============================================================

# 3.5 Voice over IP Protocols and Components

a Voice over IP (VoIP) network digitizes the spoken voice into packets and transmits those packets across a data network. This allows voice, data, and even video to share the same medium. In a network with unified communications (UC) such as voice, video, and data, specialized UC servers, controllers, devices, and gateways are also likely to be used. In a cloud computing environment, they may be virtualized as well. Figure 3-40 shows a sample VoIP network topology. Not only can a VoIP network provide significant cost savings over a traditional PBX solution, many VoIP networks offer enhanced services (for example, integration with video conferencing applications and calendaring software to determine availability) not found in traditional corporate telephony environments.  
  

![A VOIP network topology is displayed. The topology shows the following components connected horizontally via serial cable: a switch, a gateway, an IP WAN cloud, and a gateway. Both the gateways are connected to a cloud named "PSTN" at the top via serial cable. The switch is connected to an IP phone and a call agent at the top and bottom, respectively. The gateway on the right is connected to PBX. The PBX is connected to an analog phone at the bottom. A double-headed arrow labeled SIP is shown between IP phone and the call agent. A double-headed arrow labeled SIP is shown between the call agent and the gateway (left). A double-headed arrow labeled RTP is shown between IP phone and the gateway (left). Two double-headed arrows labeled SIP and RTP are shown between the two gateways.](https://s3.amazonaws.com/jigyaasa_content_static/Image3/03fig40.jpg)

![[Pasted image 20230706231031.png]]
![[Pasted image 20230706231043.png]]

- **IP phone:** Device with an integrated Ethernet connection that digitizes, packetizes, and sends voice over a data network
- **Call agent:** Repository for a voice over IP network's dial plan that analyzes dialed digits and determines the route
- **PBX:** Privately owned telephone switch, traditionally used in corporate telephony systems
- **SIP:** Manages, signals, and sets-up voice and video sessions over IP networks
- **Gateway:** Device that acts as a translator between two different telephony signaling environments
- **RTP:** A protocol that carries voice (and interactive video)
===============================================================

# 3.6 Real-World Case Study

Acme, Inc., has decided that to keep pace with the growing customer demand, it will use software as a service from a cloud provider for its primary business application. This will allow the company to focus on its business and use the application instead of managing and maintaining that application.  
  
There will be some desktop computers in the office for the users, and those computers will be networked using UTP cabling that goes to a switch. The switches on each floor of the building will be secured in a locked intermediate distribution frame (IDF) in a wiring closet on each floor. For the interconnections between the switches on each of the floors, multi mode fiber-optic cabling is used. When purchasing hardware and fiber-optic cabling, Acme will want to make sure that the fiber-optic connector type matches the correct fiber interface type on the switches. In the basement of the building is an area for Acme, Inc. to use as its own dedicated main distribution frame (MDF). From the MDF, there will be cabling that goes to the demarcation point for the service provider for the WAN and Internet connectivity provided by the service provider. This connectivity will be used to access the cloud services (SaaS specifically) from the service provider and for WAN and Internet access.  
  
Inside the building, a few of the users have mobile devices. To facilitate network access for these mobile users, wireless APs, which are physically connected through UTP cabling to the switches on each floor, will be used. Hubs will not be used because they are not very secure or effective and because all network traffic is sent to every other port on a hub, whereas a switch only forwards unicast frames to the other ports that need to see that traffic. To consolidate hardware in the MDF, multilayer switches will be used to provide not only Layer 2 forwarding of frames based on MAC addresses, but also Layer 3 forwarding of packets based on IP addresses (routing). On the LAN, Acme intends to use a set of redundant servers near the MDF to provide services such as DHCP, DNS, and time synchronization to each of its offices on each floor. The servers can coordinate DNS and time synchronization with other servers on the public Internet. The local servers can also be used for network authentication to control user access to the network regardless of the source, including wireless, wired, and VPN. Instead of purchasing multiple physical servers, the company is going to virtualize the servers onto specialized hardware that is fault tolerant. With this solution, the company can easily add additional logical servers without purchasing a physical system for every new server. This could include unified communications servers that may be involved with voice, video, and other types of streaming data.  
  
A VPN device will also be installed in the MDF to allow users who are connected to the Internet from their home or other locations to build a secure VPN remote access connection over the Internet to the corporate headquarters. Instead of buying a dedicated VPN device such as a concentrator, Acme is going to use a firewall that has this VPN capability integrated as part of its services.


===============================================================

# Glossary

#### coaxial cable

Also known as _coax_, a coaxial cable is composed of two conductors. One of the conductors is an inner insulated conductor. This inner conductor is surrounded by another conductor. This second conductor is sometimes made of a metallic foil or woven wire.

#### twisted-pair cable

Today's most popular media type is twisted-pair cable, where individually insulated copper strands are intertwined into a twisted-pair cable. Two categories of twisted-pair cable include shielded twisted pair (STP) and unshielded twisted pair (UTP).

#### shielded twisted-pair (STP) cable

STP cabling prevents wires in a cable from acting as an antenna, which might receive or transmit EMI. STP cable might have a metallic shielding, similar to the braided wire that acts as an outer conductor in a coaxial cable.

#### unshielded twisted-pair (UTP) cable

Blocks EMI from the copper strands making up a twisted-pair cable by having more tightly twisted strands (that is, more twists per centimeter). Because these strands are wrapped around each other, the wires insulate each other from EMI.

#### electromagnetic interference (EMI)

An electromagnetic waveform that can be received by network cable (possibly corrupting data traveling on the cable) or radiated from a network cable (possibly interfering with data traveling on another cable).

#### plenum

Plenum cabling is fire retardant and minimizes toxic fumes released by network cabling if that cable were to catch on fire. As a result, plenum cabling is often a requirement of local fire codes for cable in raised flooring or in other open-air return ducts.

#### multimode fiber (MMF)

Multimode fiber-optic cabling has a core with a diameter large enough to permit the injection of light at multiple angles. The different paths (that is, _modes_) that light travels can lead to multimode delay distortion, which causes bits to be received out of order because the pulses of light representing the bits traveled different paths (and therefore different distances).

#### single-mode fiber (SMF)

SMF cabling has a core with a diameter large enough to permit only a single path for light pulses (that is, only one mode of propagation). By having a single path for light to travel, SMF eliminates the concern of multimode delay distortion.

#### 66 block

Traditionally used in corporate environments for cross-connecting phone system cabling. As 10Mbps LANs started to grow in popularity in the late 1980s and early 1990s, these termination blocks were used to cross-connect Category 3 UTP cabling. The electrical characteristics (specifically, crosstalk) of a 66 block, however, do not support higher-speed LAN technologies, such as 100Mbps Ethernet networks.

#### 110 block

Because 66 blocks are subject to too much crosstalk for higher-speed LAN connections, 110 blocks can be used to terminate a cable (such as a Category 5 cable) being used for those higher-speed LANs.

#### multilayer switch

Like a router, a multilayer switch can make traffic forwarding decisions based on Layer 3 information. Although multilayer switches more closely approach wire-speed throughput than most routers, routers tend to have a greater feature set and are capable of supporting more interface types than a multilayer switch.

#### firewall

Primarily a network security appliance, a firewall can protect a trusted network (for example, a corporate LAN) from an untrusted network (for example, the Internet) by allowing the trusted network to send traffic into the untrusted network and receive the return traffic from the untrusted network, while blocking traffic for sessions that were initiated on the untrusted network.

#### Domain Name System (DNS) server

Performs the task of taking a domain name (for example, [www.ciscopress.com](http://www.ciscopress.com/)) and resolving that name into a corresponding IP address (for example, 10.1.2.3).

#### Dynamic Host Configuration Protocol (DHCP)

Dynamically assigns IP address information (for example, IP address, subnet mask, DNS server's IP address, and default gateway's IP address) to network devices.

#### proxy server

Intercepts requests being sent from a client and forwards those requests on to their intended destination. The proxy server then sends any return traffic to the client that initiated the session. This provides address hiding for the client. Also, some proxy servers conserve WAN bandwidth by offering a content-caching function. In addition, some proxy servers offer URL filtering to, for example, block users from accessing social networking sites during working hours.

#### content engine

A dedicated appliance whose role is to locally cache content received from a remote network (for example, a destination on the Internet). Subsequent requests for that content can be serviced locally, from the content engine, thus reducing bandwidth demand on a WAN.

#### content switch

Can be used to load-balance requests for content across a group of servers containing that content. If one of the servers in the group needs to have maintenance performed, that server could be administratively removed from the group, as defined on the content switch. As a result, the content switch can help maximize uptime when performing server maintenance. It minimizes the load on individual servers by distributing its load across multiple identical servers. A content switch also allows a network to scale because one or more additional servers could be added to the server group defined on the content switch if the load on existing servers increases.

#### virtual server

Allows a single physical server to host multiple virtual instances of various operating systems. This allows, for example, a single physical server to simultaneously host multiple Microsoft Windows servers and multiple Linux servers.

#### virtual switch

Performs Layer 2 functions (for example, VLAN separation and filtering) between various server instances running on a single physical server.

#### virtual desktop

A virtual desktop solution allows a user to store data in a centralized data center, as opposed to the hard drive of his local computer. Then, with appropriate authentication credentials, that user can access his data from various remote devices (for example, his smartphone or another computer).

#### onsite

The term _onsite_ in the context of virtualization technologies refers to hosting virtual devices on hardware physically located in a corporate data center.

#### offsite

The term _offsite_ in the context of virtualization technologies refers to hosting virtual devices on hardware physically located in a service provider's data center.

#### network as a service (NaaS)

A service provider offering where clients can purchase data services (for example, email, LDAP, and DNS services) traditionally hosted in a corporate data center.

#### virtual PBX

Usually a VoIP telephony solution hosted by a service provider, which interconnects with a company's existing telephone system.

#### Session Initiation Protocol (SIP)

A VoIP signaling protocol used to set up, maintain, and tear down VoIP phone calls.

#### Real-time Transport Protocol (RTP)

A Layer 4 protocol that carries voice (and interactive video).

#### software as a service (SaaS)

Providing applications or application services via the cloud.

#### platform as a service (PaaS)

This category of cloud permits the delivery of operating systems and libraries needed by developers.

#### infrastructure as a service (IaaS)

Providing network infrastructure as a service using cloud technologies.

#### IP Address Management

The software and processes for managing the IP addresses used in an organization.

#### software-defined networking (SDN)

An approach to computer networking that allows network administrators to programmatically initialize, control, change, and manage network behavior dynamically via open interfaces and provide abstraction of lower-level functionality.

#### software-defined networking (SDN) controller

Often referred to as the "brains" of the SDN network, this device sends commands to the network devices to have configurations made.

#### Z-Wave

A wireless communications protocol used primarily for home automation. It is a mesh network using low-energy radio waves to communicate from appliance to appliance, allowing for wireless control of residential appliances and other devices, such as lighting control, security systems, thermostats, windows, locks, swimming pools, and garage door openers.

#### ANT+

A wireless protocol for monitoring sensor data such as a person's heart rate or a car's tire pressure, as well as for controlling systems such as indoor lighting and television sets. ANT+ is designed and maintained by the ANT+ Alliance, which is owned by Garmin. It is based on the ANT protocol.

#### Bluetooth

A wireless protocol for creating a personal area network, where a device such as a mobile phone can send data to a headset, for example.

#### Near Field Communication (NFC)

A wireless communications technology that might be seen in the Internet of Things. This technology is often used in payment systems.

#### infrared (IR)

A wireless line-of-sight technology that might be found in an Internet of Things deployment.

#### radio-frequency identification (RFID)

Radio-frequency identification (RFID) uses electromagnetic fields to automatically identify and track tags attached to objects. The tags contain electronically stored information.

#### wireless range extender

Since all 802.11 wireless technologies have distance limitations, a wireless range extender can amplify the signal and extend the reachability of a wireless cell.

#### next-generation firewall (NGFW)

More modern firewalls that can perform tasks such as deep packet inspection.

#### Fibre Channel over Ethernet (FCoE)

Technology that permits SAN traffic of FC over the Ethernet media.

#### Network Access Server (NAS)

A network device specialized in controlling access to the network. NAS might also stand for network-attached storage.

#### storage area network (SAN)

A specialized network for the storage of data.

===============================================================

===============================================================