
# 1.1 DEFINING A NETWORK
- purpose of a network: make conection
![[Pasted image 20230603211832.png]]

## OVERVIEW OF NETWORK COMPONENTS
![[Pasted image 20230603211915.png]]
- **Client** : end user 
- **Server:** serves up resource to a network
- **Hub:** older technology that interconnects network components such as clients and servers
- Switch: interconnects network components
- Router: Layer 3 device, forwarding decision based on logical network addresses
- Media: "cables, wireless"
- WAN Link

![[Pasted image 20230603212359.png]]

# 1.2 NETWORK DEFINED BY GEOGRAPHY
Based on the geographic dispersion of network components, you can classify networks into various categories, including the following:
- Local area network (LAN)
- Wide area network (WAN)
- Wireless local area network (WLAN)
- Storage area network (SAN)
- Campus area network (CAN)
- Metropolitan area network (MAN)
- Personal area network (PAN)

### LAN
A LAN interconnects network components within a local area (for example, within a building). Examples of common LAN technologies you are likely to meet include Ethernet (that is, IEEE 802.3) and wireless networks (that is, IEEE 802.11)
![[Pasted image 20230603212759.png]]

### WAN
A WAN interconnects network components that are geographically separated. For example, a corporate headquarters might have multiple WAN connections to remote office sites. Multiprotocol Label Switching (MPLS) and Asynchronous Transfer Mode (ATM) are examples of WAN technologies.
![[Pasted image 20230603212947.png]]

### WLAN
A local area network made up of wireless networking devices is a wireless local area network (WLAN). Lesson 8, "Wireless Technologies," deals with this topic in detail.

### SAN
You can construct a high-speed, highly reliable network for the express purpose of transmitting stored data. This network is called a storage area network.

## Other Categories of Networks

### **CAN**  
A controller area network (CAN) is a robust vehicle bus standard designed to enable microcontrollers and devices to communicate with each other's applications without needing a host computer. It provides an economical and strong network that helps multiple CAN devices communicate with one another. It was originally developed within the automotive industry to replace the complex electrical wiring harness with a two-wire data bus.  
  
### **MAN**  
More widespread than a CAN and less widespread than a WAN, a MAN interconnects locations scattered throughout a metropolitan area. Imagine, for example, that a business in Chicago has a location near O'Hare Airport, another location near the Navy Pier, and another location in the Willis Tower (previously known as the Sears Tower). If a service provider could interconnect those locations using a high-speed network, such as a 10Gbps (that is, 10 billion bits per second) network, the interconnection of those locations would form a MAN. One example of a MAN technology is Metro Ethernet, which features much higher speeds than the traditional WAN technologies that might have been used in the past to connect such locations.  
  
### **PAN**  
A PAN is a network whose scale is even smaller than a LAN. For example, a connection between a PC and a digital camera via a universal serial bus (USB) cable could be considered a PAN. Another example is a PC connected to an external hard drive via a FireWire connection. A PAN, however, is not necessarily a wired connection. A Bluetooth connection between your cell phone and your car's audio system is considered a wireless PAN (WPAN). The main distinction of a PAN, however, is that its range is typically limited to just a few meters.


# 1.3 NETWORK DEFINED BY TOPOLOGY

### Physical vs Logical Topology
The actual traffic flow decides the **_logical topology_**, 
whereas the way components are physically interconnected determines the **_physical topology_.**

Token Rung **MEDIA ACCESS UNIT (MAU)**
![[Pasted image 20230603222722.png]]

### BUS TOPOLOGY
![[Pasted image 20230603223112.png]]


![[Pasted image 20230603223254.png]]
![[Pasted image 20230603223519.png]]

### RING TOPOLOGY
circular fashion around a closed network loop. typically sends data in single direction to each connected device in turn
![[Pasted image 20230603223715.png]]

Token Ring, however, was not the only popular ring-based topology popular in networks back in the 1990s. Fiber Distributed Data Interface (FDDI) was another variant of a ring-based topology. Most FDDI networks (which, as the name suggests, have fiber optics as the media) used not just one ring, but two. These two rings sent data in opposite directions, resulting in _counter-rotating rings_. One benefit of counter-rotating rings was that if a fiber broke, the stations on each side of the break could interconnect their two rings, resulting in a single ring capable of reaching all stations on the ring.

![[Pasted image 20230603223802.png]]
![[Pasted image 20230603223821.png]]

### STAR TOPOLOGY
hub at the center, typical hub back in the early 1990s, modern network uses switch in the center of the star.
![[Pasted image 20230603223925.png]]

![[Pasted image 20230603223942.png]]

### HUB and SPOKE TOPOLOGY
interconnecting multiple sites via WAN links. a HUB site with multiple outside sites
![[Pasted image 20230603224059.png]]
similar to the star topology used in LANs

minimize WAN expenses by not directly connecting any two spoke location
![[Pasted image 20230603224155.png]]


### FULL MESH TOPOLOGY
Hub and Spoke topo lacked redundancy and suffered from suboptimal routes.
Full mesh directly connects every sites to every other sites
![[Pasted image 20230603224513.png]]
- optimal path can be selected
- highly fault tolerant
![[Pasted image 20230603224615.png]]

### PARTIAL MESH TOPOLOGY
Partial mesh WAN topology. (does not connect ever sides to ever sides)
must consider traffic patterns and strategically add links interconnecting sites that hae higher volumes and traffic between themselves
![[Pasted image 20230603224707.png]]
![[Pasted image 20230603224809.png]]




### Explanation
The following are correct statements about hub-and-spoke and partial mesh topologies:
-   In the hub-and-spoke topology, each remote site connects back to the main site via a WAN link.
-   The hub-and-spoke topology lacks redundancy because each remote site is reachable by only a single WAN link.
-   The partial mesh topology uses fewer links than a full mesh topology but more links than the hub-and-spoke topology for interconnecting the same number of sites.
-   The partial mesh topology is more redundant than the hub-and-spoke topology.
-   In the hub-and-spoke topology, adding additional sites is easy as compared to the partial mesh topology.




# 1.4 WIRELESS TOPOLOGIES

#### Ad Hoc (PEER TO PEER)
The simplest of wireless topologies is the ad hoc wireless network. **This means that the wireless nodes are in charge of sending and receiving traffic to each other, without the assistance of infrastructure devices, such as switches or access points.** Some network engineers refer to the ad hoc topology as simply a wireless peer-to-peer (P2P) type of network. One common example of an ad hoc wireless network would be Apple's AirDrop, used to send files between two smartphones. This author prefers the more formal and specific ad hoc terminology. Your Network+ exam does as well! The opposite of this approach is an infrastructure topology, which is discussed next.

#### Infrastructure (communicate to each other through WAP)
With the infrastructure topology, you have specialized wireless equipment for permitting the wireless communications to take place. Many homes today feature a wireless local area network (WLAN). **A wireless access point (WAP) allows the various computers (and other wireless devices) to communicate with each other through the WAP acting like a hub device.** This WAP connects to the service provider (SP) of the home user with a wired connection. For example, a coaxial cable could connect to the broadband cable service for high-speed Internet connectivity.

#### Mesh
A specific type of ad hoc wireless topology is the mesh. This topology is more sophisticated than the ad hoc in that specialized nodes help move the traffic throughout the topology. Note that these devices are not as fancy as the access points found in an infrastructure type of topology. The first wireless mesh topology I ever had the pleasure of working on was one that could adequately provide coverage for a large recreational vehicle (RV) park. Obvious challenges with this design came in the form of interference and the nodes' ability to sustain harsh environmental conditions often found in Florida, USA. Yes, that would be sun and the occasional tropical storm.

# 1.5 Networks Defined by Resource Location
### Client / Server Networks
- Dedicated server gives shared access to files, and networked printer is available as a resource to the network's client. commonly used in businesses
- can be better than the one of peer-to-peer network, because resource can be located on a dedicated servers rather than on a PC running a variety of end-user applications. 
![[Pasted image 20230608161510.png]]

![[Pasted image 20230608161608.png]]

A server in a client/server network could be a computer running a network operating system (NOS) such as a Linux Server or one of the Microsoft Windows Server operating systems. Alternatively, a server might be a host making its file system available to remote clients via the Network File System (NFS) service, which was originally developed by Sun Microsystems.

A variant of the traditional server in a client/server network, where the server provides shared file access, is a network-attached storage (NAS). A NAS device is a mass storage device that attaches directly to a network. Rather than running an advanced NOS, a NAS device usually makes files available to network clients via a service such as NFS.

### Peer-to-Peer Networks
Peer-to-peer networks allow interconnected devices (for example, PCs) to share their resources with one another. Those resources could be, for example, files or printers

![[Pasted image 20230608161732.png]]
Peer-to-peer networks are seen in smaller businesses and in homes. The popularity of these peer-to-peer networks is fueled in part by client operating systems that support file and print sharing. Scalability for peer-to-peer networks is a concern, however. Specifically, as the number of devices (that is, peers) increases, the administration burden increases. For example, a network administrator might have to manage file permissions on multiple devices, as opposed to a single server.

![[Pasted image 20230608161755.png]]
Some networks have characteristics of both peer-to-peer and client/server networks. For example, all PCs in a company might point to a centralized server for accessing a shared database in a client/server topology. However, these PCs might simultaneously share files and printers with one another in a peer-to-peer topology. Such a network, which has a mixture of client/server and peer-to-peer characteristics, is called a _hybrid_ network.

Here are the network types:
- **Client/server**
    - Resource sharing through dedicated hardware
    - Highly scalable
    - Contains a single point of failure because multiple clients might rely on a single server for their resources
- **Peer-to-peer**
    - Resource sharing through clients' OS
    - Easy installation
    - Costs lesser because there is no requirement for dedicated server resources

# GLOSSARY

#### client
Defines the device an end user uses to access a network. This device might be a workstation, laptop, smartphone with wireless capabilities, tablet, or variety of other end-user terminal devices.

#### server
As its name suggests, a server serves up resources to a network. These resources might include email access as provided by an email server, web pages as provided by a web server, or files available on a file server.

#### hub
An Ethernet hub is an older technology used to interconnect network components, such as clients and servers. Hubs vary in their number of available ports. A hub does not perform an inspection of the traffic it passes. Rather, a hub simply receives traffic in a port and repeats that traffic out all of its other ports.

#### switch
Like an Ethernet hub, an Ethernet switch interconnects network components. Like a hub, switches are available with a variety of port densities. However, unlike a hub, a switch doesn't simply take traffic in on one port and forward copies of that traffic out all other ports. Rather, a switch learns which devices reside off of which ports. As a result, when traffic comes in a switch port, the switch interrogates the traffic to see where it's destined. Then, based on what the switch has learned, it forwards the traffic out of the appropriate port and not out all of the other ports.

#### router
A router is considered a Layer 3 device, meaning that it makes its forwarding decisions based on logical network addresses. Most modern networks use IP addressing.

#### media
Devices need to be interconnected via some sort of media. This media could be copper cabling. Alternatively, it could be a fiber-optic cable. Media might not even be a cable, as is the case with wireless networks, where radio waves travel through the media of _air_.

#### wide area network (WAN) link
An interconnection between two devices in a WAN.

#### local area network (LAN)
Interconnects network components within a local region (for example, within a building).

#### wide area network (WAN)
Interconnects network components that are geographically separated.

#### campus area network (CAN)
An interconnection of networks located in nearby buildings (for example, buildings on a college campus).

#### metropolitan area network (MAN)
Interconnects locations scattered throughout a metropolitan area.

#### personal area network (PAN)
A network whose scale is smaller than a LAN. As an example, a connection between a PC and a digital camera via a USB cable is considered to be a PAN.

#### wireless local area network (WLAN)
A local area network made up of wireless networking devices is a wireless local area network (WLAN).

#### storage area network (SAN)
A specialized network for the storage of data.

#### logical topology
The actual traffic flow of a network determines the network's logical topology.

#### physical topology
The way a network's components are physically interconnected determines the network's physical topology.

#### bus topology
Typically, this topology uses a cable running through the area requiring connectivity, and devices to be networked can tap into that cable.

#### ring topology
In a ring topology, traffic flows in a circular fashion around a closed network loop (that is, a ring). Typically, a ring topology sends data, in a single direction, to each connected device in turn, until the intended destination receives the data.

#### star topology
In a star topology, a network has a central point (for example, a switch) from which all attached devices radiate.

#### hub-and-spoke topology
When interconnecting multiple sites (for example, multiple corporate locations) via WAN links, a hub-and-spoke topology has a WAN link from each remote site (a spoke site) to the main site (the hub site).

#### full-mesh topology
Directly connects every site to every other site.

#### partial-mesh topology
A hybrid of a hub-and-spoke topology and a full-mesh topology. A partial-mesh topology can be designed to provide an optimal route between selected sites, while avoiding the expense of interconnecting every site to every other site.

#### ad hoc topology
The simplest of wireless topologies is the ad hoc wireless network. This means that the wireless nodes are in charge of sending and receiving traffic to each other, without the assistance of infrastructure devices, such as switches or access points.

#### client/server network
In a client/server network, a dedicated server (for example, a file server or a print server) provides shared access to a resource (for example, files or a printer). Clients (for example, PCs) on the network with appropriate privilege levels can gain access to those shared resources.

#### peer-to-peer network
Allows interconnected devices (for example, PCs) to share their resources with one another. These resources could be, for example, files or printers.