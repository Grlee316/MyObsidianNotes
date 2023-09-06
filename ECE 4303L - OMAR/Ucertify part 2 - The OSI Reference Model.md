This lesson defines those seven layers and offers examples of what you might find at each layer. It also contrasts the OSI model with another model—the TCP/IP stack, also known as the Department of Defense (DoD) model—that focuses on Internet Protocol (IP) communications.

# 2.1. The Purpose of Reference Models
- **Layer 1:** The physical layer
- **Layer 2:** The data link layer
- **Layer 3:** The network layer
- **Layer 4:** The transport layer
- **Layer 5:** The session layer
- **Layer 6:** The presentation layer
- **Layer 7:** The application layer

A top-down (that is, starting at the top of the stack with Layer 7 and working your way down to Layer 1) acrostic is **_A_**_ll_ **_P_**_eople_ **_S_**_eem_ **_T_**_o_ **_N_**_eed_ **_D_**_ata_ **_P_**_rocessing_. As a couple of examples, using this acrostic, the _A_ in *A*ll reminds us of the _A_ in *A*pplication, and the _P_ in *P*eople reminds us of the _P_ in *P*resentation. Another common memory aid is **_P_**_lease_ **_D_**_o_ **_N_**_ot_ **_T_**_hrow_ **_S_**_ausage_ **P**_izza_ **_A_**_way_, which begins at Layer 1 and works its way up to Layer 7.

At the physical layer, binary expressions (that is, a series of 1s and 0s) represent data. A binary expression is created using bits, where a bit is a single 1 or a single 0. At lower layers, however, bits are grouped together, into what is known as a _protocol data unit_ (PDU) or a _data service unit_.

Engineers tend to use the term _packet_ generically to refer to these PDUs. However, PDUs might have an added name, depending on their OSI layer. Figure 2-3 illustrates these PDU names. A common memory aid for these PDUs is **_S_**_ome_ **_P_**_eople_ **_F_**_ear_ **_B_**_irthdays_, where the _S_ in *S*ome reminds us of the _S_ in *S*egments. The *P* in *P*eople reminds us of the _P_ in *P*ackets, and the _F_ in *F*ear reflects the _F_ in *F*rames. Finally, the _B_ in *B*irthdays reminds us of the _B_ in *B*its.

Transport -> Segments
Network -> Packets
Data Link -> Frames
Physical -> Bits

![[Pasted image 20230612220928.png]]

### Physical Layer

![[Pasted image 20230617234011.png]]

The physical layer defines the following:

- **How to represent bits on the medium:** Data on a computer network is represented as a binary expression. Lesson 5,"IPv4 and IPv6 Addresses," discusses binary in much more detail. Electrical voltage (on copper wiring) or light (carried via fiber-optic cabling) can represent these 1s and 0s.  
      
    For example, the presence or the absence of voltage on a wire portrays a binary 1 or a binary 0, respectively, as illustrated in Figure 2-5. Similarly, the presence or absence of light on a fiber-optic cable renders a 1 or 0 in binary. This type of approach is called _current state modulation_.  
      
    
    ![The figure shows a graph illustrating the current state modulation. The horizontal axis of the graph is labeled as time and the vertical axis of the graph is labeled as voltage. The graph value in the horizontal axis is marked as follows: 0 0 1 1 1 0 1 0 1 and 0. The graph value in the vertical axis is marked from minus 5 to plus 5.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig05.jpg)
    
    Figure 2-5: Current State Modulation
    
      
    An alternate approach to portraying binary data is _state transition modulation_, as shown in Figure 2-6, where the transition between voltages or the presence of light shows a binary value.  
      
    
    ![The figure shows a graph illustrating the transition modulation. The horizontal axis of the graph is labeled as time and the vertical axis of the graph is labeled as voltage. The graph value in the horizontal axis is marked as follows: 0 1 0 1 1 1 1 1 and 1. The graph value in the vertical axis is marked from minus 5 to plus 5.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig06.jpg)
    
    Figure 2-6: Transition Modulation
    

Note

Other modulation types you might be familiar with from radio include amplitude modulation (AM) and frequency modulation (FM). AM uses a variation in a waveform's amplitude (that is, signal strength) to portray the original signal. However, FM uses a variation in frequency to stand for the original signal.

- **Wiring standards for connectors and jacks:** Lesson 3,"Network Components," describes several standards for network connectors. For example, the TIA/EIA-568-B standard describes how to wire an RJ-45 connector for use on a 100BASE-TX Ethernet network, as shown in Figure 2-7.  
      
    
    ![The figure shows the TIA/EIA-568-B Wiring Standard for an RJ-45 Connector. The connector shows eight pins labeled pin 1 to pin 8 from the bottom to the top. The colors of each pin from bottom to top are as follows: O/W, O, Gr/W, BI, B/W, Gr, Br/W, and Br.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig07.jpg)
    
    Figure 2-7: TIA/EIA-568-B Wiring Standard for an RJ-45 Connector
    
- **Physical topology:** Layer 1 devices view a network as a physical topology (as opposed to a logical topology). Examples of a physical topology include bus, ring, and star topologies, as described in Lesson 1, "Computer Network Fundamentals."
- **Synchronizing bits:** For two networked devices to successfully communicate at the physical layer, they must agree on when one bit stops and another bit starts. Specifically, the devices need a method to synchronize the bits. Two basic approaches to bit synchronization include _asynchronous_ and _synchronous_ synchronization:
    - **Asynchronous:** With this approach, a sender states that it is about to start transmitting by sending a start bit to the receiver. When the receiver sees this, it starts its own internal clock to measure the next bits. After the sender transmits its data, it sends a stop bit to say that it has finished its transmission.
    - **Synchronous:** This approach synchronizes the internal clocks of both the sender and the receiver to ensure that they agree on when bits begin and end. A common approach to make this synchronization happen is to use an external clock (for example, a clock given by a service provider). The sender and receiver then reference this external clock.
- **Bandwidth usage:** The two fundamental approaches to bandwidth usage on a network are _broadband_ and _baseband_:
    - **Broadband:** Broadband technologies divide the bandwidth available on a medium (for example, copper or fiber-optic cabling) into different channels. A sender can then transmit different communication streams over the various channels. For example, consider frequency-division multiplexing (FDM) used by a cable modem. Specifically, a cable modem uses certain ranges of frequencies on the cable coming into your home from the local cable company to carry incoming data, another range of frequencies for outgoing data, and several other frequency ranges for various TV stations.
    - **Baseband:** Baseband technologies, in contrast, use all the available frequencies on a medium to send data. Ethernet is an example of a networking technology that uses baseband.
- **Multiplexing strategy:** Multiplexing allows multiple communications sessions to share the same physical medium. Cable TV, as previously mentioned, allows you to receive multiple channels over a single physical medium (for example, a coaxial cable plugged into the back of your television). Here are some of the more common approaches to multiplexing:
    - **Time-division multiplexing (TDM):** TDM supports different communication sessions (for example, different telephone conversations in a telephony network) on the same physical medium by causing the sessions to take turns. For a brief period, defined as a _time slot_, data from the first session is sent, followed by data from the second session. This continues until all sessions have had a turn, and the process repeats itself.
    - **Statistical time-division multiplexing (StatTDM):** A downside to TDM is that each communication session receives its own time slot, even if one of the sessions does not have any data to send at the moment. To make a more efficient use of available bandwidth, StatTDM dynamically assigns time slots to communications sessions on an as-needed basis.
    - **Frequency-division multiplexing (FDM):** FDM divides a medium's frequency range into channels, and different communication sessions send their data over different channels. As previously described, this approach to bandwidth usage is called _broadband_.

Examples of devices defined by physical layer standards include hubs, wireless access points, and network cabling.  
  

Note

A hub interconnects PCs in a LAN. However, it is considered a physical layer device because a hub takes bits coming in on one port and retransmits those bits out of all other ports. At no point does the hub interrogate any addressing information in the data.

  
### Data Link Layer
The data link layer is concerned with the following:

- Packaging data into frames and transmitting those frames on the network
- Performing error detection/correction
- Uniquely finding network devices with an address
- Handling flow control

These processes are referred to collectively as _data link control_ (DLC) and are illustrated in Figure 2-8.  
  

![The figure depicts the key features of the data link layer. The illustration shows the seven layers of the OSI model as a stack. The data link layer is divided into two sublayers: MAC and LLB. The key features of the MAC layer are listed beside it that reads as follows: Physical addressing, Logical topology, and Method of transmitting on the media. The key features of the LLB layer are listed beside it that reads as follows: Connection services and Synchronizing transmissions.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig08.jpg)

Figure 2-8: Layer 2-The Data Link Layer

**Media Access Control**  
Characteristics of the Media Access Control (MAC) sublayer include the following:

- **Physical addressing:** A common example of a Layer 2 address is a MAC address, which is a 48-bit address assigned to a device's network interface card (NIC). MAC addresses are written in hexadecimal notation (for example, 58:55:ca:eb:27:83). The first 24 bits of the 48-bit address is the _vendor code_. The IEEE Registration Authority assigns a manufacturer one or more unique vendor codes. You can use the list of vendor codes at [http://standards.ieee.org/develop/regauth/oui/oui.txt](http://standards.ieee.org/develop/regauth/oui/oui.txt) to identify the manufacturer of a networking device, based on the first half of the device's MAC address. The last 24 bits of a MAC address are assigned by the manufacturer, and they act as a serial number for the device. No two MAC addresses in the world should have the same value.
- **Logical topology:** Layer 2 devices view a network as a logical topology. Examples of a logical topology include bus and ring topologies, as described in Lesson 1.
- **Method of transmitting on the media:** With several devices connected to a network, there needs to be some strategy for deciding when a device sends on the media. Otherwise, multiple devices might send at the same time and thus interfere with one another's transmissions.

**Logical Link Control**  
Characteristics of the Logical Link Control (LLC) sublayer include the following:

- **Connection services:** When a device on a network receives a message from another device on the network, that recipient device can give feedback to the sender in the form of an acknowledgment message. The two main functions provided by these acknowledgment messages are as follows:
    - **Flow control:** Limits the amount of data a sender can send at one time; this prevents the sender from overwhelming the receiver with too much information.
    - **Error control:** Allows the recipient of data to let the sender know whether the expected data frame was not received or whether it was received but is corrupted. The recipient figures out whether the data frame is corrupt by mathematically calculating a checksum of the data received. If the calculated checksum does not match the checksum received with the data frame, the recipient of the data draws the conclusion that the data frame is corrupted and can then notify the sender via an acknowledgment message.
- **Synchronizing transmissions:** Senders and receivers of data frames need to coordinate when a data frame is being transmitted and should be received. The three methods of performing this synchronization are detailed here:
    - **Isochronous:** With isochronous transmission, network devices look to a common device in the network as a clock source, which creates fixed-length time slots. Network devices can determine how much free space, if any, is available within a time slot and then insert data into an available time slot. A time slot can accommodate more than one data frame. Isochronous transmission does not need to provide clocking at the beginning of a data string (as does synchronous transmission) or for every data frame (as does asynchronous transmission). As a result, isochronous transmission uses little overhead when compared to asynchronous or synchronous transmission methods.
    - **Asynchronous:** With asynchronous transmission, network devices reference their own internal clocks, and network devices do not need to synchronize their clocks. Instead, the sender places a start bit at the beginning of each data frame and a stop bit at the end of each data frame. These start and stop bits tell the receiver when to monitor the medium for the presence of bits.  
          
        An additional bit, called the _parity bit_, might also be added to the end of each byte in a frame to detect an error in the frame. For example, if even parity error detection (as opposed to odd parity error detection) is used, the parity bit (with a value of either 0 or 1) would be added to the end of a byte, causing the total number of 1s in the data frame to be an even number. If the receiver of a byte is configured for even parity error detection and receives a byte where the total number of bits (including the parity bit) is even, the receiver can conclude that the byte was not corrupted during transmission.

Note

Using a parity bit to detect errors might not be effective if a byte has more than one error (that is, more than one bit that has been changed from its original value).

- **Synchronous:** With synchronous transmission, two network devices that want to communicate between themselves must agree on a clocking method to show the beginning and ending of data frames. One approach to providing this clocking is to use a separate communications channel over which a clock signal is sent. Another approach relies on specific bit combinations or control characters to indicate the beginning of a frame or a byte of data.  
      
    Like asynchronous transmissions, synchronous transmissions can perform error detection. However, rather than using parity bits, synchronous communication runs a mathematical algorithm on the data to create a cyclic redundancy check (CRC). If both the sender and the receiver calculate the same CRC value for the same chunk of data, the receiver can conclude that the data was not corrupted during transmission.

Examples of devices defined by data link layer standards include switches, bridges, and NICs.


### The Network Layer
The network layer, as shown in Figure 2-9, is primarily concerned with forwarding data based on logical addresses.  
  
![The figure depicts the key features of the network layer. The illustration shows the seven layers of the OSI model as a stack. The key features of the network layer are listed beside it that reads as follows: Logical addressing, Switching, Route discovery and selection, Connection services, Bandwidth usage, and Multiplexing strategy.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig09.jpg)

Although many network administrators think of routing and IP addressing when they hear about the network layer, this layer is actually responsible for a variety of tasks:

- **Logical addressing:** Whereas the data link layer uses physical addresses to make forwarding decisions, the network layer uses logical addressing to make forwarding decisions. A variety of routed protocols (for example, AppleTalk and IPX) have their own logical addressing schemes, but by far, the most widely deployed routed protocol is Internet Protocol (IP). Lesson 5 discusses IP addressing in detail.
- **Switching:** Engineers often associate the term _switching_ with Layer 2 technologies; however, the concept of switching also exists at Layer 3. Switching, at its essence, is making decisions about how data should be forwarded. At Layer 3, three common switching techniques exist:
    - **Packet switching:** With packet switching, a data stream is divided into packets. Each packet has a Layer 3 header that includes a source and destination Layer 3 address. Another term for packet switching is _routing_, which is discussed in more detail in Lesson 6, "Routing IP Packets."
    - **Circuit switching:** Circuit switching dynamically brings up a dedicated communication link between two parties for those parties to communicate.  
          
        As a simple example of circuit switching, think of making a phone call from your home to a business. Assuming you have a traditional landline servicing your phone, the telephone company's switching equipment interconnects your home phone with the phone system of the business you are calling. This interconnection (that is, _circuit_) only exists for the duration of the phone call.
    - **Message switching:** Unlike packet switching and circuit switching technologies, message switching is usually not well suited for real-time applications because of the delay involved. Specifically, with message switching, a data stream is divided into messages. Each message is tagged with a destination address, and the messages travel from one network device to another network device on the way to their destination. Because these devices might briefly store the messages before forwarding them, a network using message switching is sometimes called a _store-and-forward_ network. Metaphorically, you could visualize message switching like routing an email message, where the email message might be briefly stored on an email server before being forwarded to the recipient.
- **Route discovery and selection:** Because Layer 3 devices make forwarding decisions based on logical network addresses, a Layer 3 device might need to know how to reach various network addresses. For example, a common Layer 3 device is a router. A router can maintain a routing table indicating how to forward a packet based on the packet's destination network address.  
      
    A router can have its routing table populated via manual configuration (that is, by entering static routes), via a dynamic routing protocol (for example, RIP, OSPF, or EIGRP), or simply by the fact that the router is directly connected to certain networks.  
    
- **Connection services:** Just as the data link layer offers connection services for flow control and error control, connection services also exist at the network layer. Connection services at the network layer can improve the communication reliability, if the data link's LLC sublayer is not performing connection services.

The following functions are performed by connection services at the network layer:

- **Flow control (also known as congestion control):** Helps prevent a sender from sending data more rapidly than the receiver is capable of receiving it.
- **Packet reordering:** Allows packets to be placed in the proper sequence as they are sent to the receiver. This might be necessary because some networks support load balancing, where multiple links are used to send packets between two devices. Because multiple links exist, packets might arrive out of order.

### The Transport Layer
The transport layer, as shown in Figure 2-10, acts as a dividing line between the upper layers and lower layers of the OSI model. Specifically, messages are taken from upper layers (Layers 5–7) and are encapsulated into segments for transmission to the lower layers (Layers 1–3). Similarly, data streams coming from lower layers are de-encapsulated and sent to Layer 5 (the session layer), or some other upper layer, depending on the protocol.  
  

![The figure depicts the key features of the transport layer. The illustration shows the seven layers of the OSI model as a stack. The key features of the transport layer are listed beside it that reads as follows: TCP/UDP Windowing, and Buffering.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig10.jpg)

Two common transport layer protocols are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP):

- **Transmission Control Protocol (TCP):** A connection-oriented transport protocol. Connection-oriented transport protocols offer reliable transport, in that if a segment is dropped, the sender can detect that drop and retransmit the dropped segment. Specifically, a receiver acknowledges segments that it receives. Based on those acknowledgments, a sender can decide which segments were successfully received and which segments need to be transmitted again.
- **User Datagram Protocol (UDP):** A connectionless transport protocol. Connectionless transport protocols offer unreliable transport, in that if a segment is dropped, the sender is unaware of the drop, and no retransmission occurs.

Just as Layer 2 and Layer 3 offer flow control services, flow control services also exist at Layer 4. Two common flow control approaches at Layer 4 are windowing and buffering:

- **Windowing:** TCP communication uses windowing, in that one or more segments are sent at one time, and a receiver can attest to the receipt of all the segments in a window with a single acknowledgment. In some cases, as illustrated in Figure 2-11, TCP uses a sliding window, where the window size begins with one segment. If there is a successful acknowledgment of that one segment (that is, the receiver sends an acknowledgment asking for the next segment), the window size doubles to two segments. Upon successful receipt of those two segments, the next window holds four segments. This exponential increase in window size continues until the receiver does not acknowledge successful receipt of all segments within a certain amount of time—known as the _round-trip time_ (RTT), which is sometimes called _real transfer time_—or until a configured maximum window size is reached.  
      
    
    ![The figure shows the TCP sliding window. The illustration shows a sender on the left and a receiver on the right. A section titled as window size shows an arrow labeled segment 1 from the sender that points to the receiver. An arrow labeled ACK 2 from the receiver points to the sender. A section labeled as window size 2 shows two arrows labeled segment 2 and segment 3 from the sender that points to the receiver. An arrow labeled ACK 4 from the receiver points to the sender. A section titled as window size 4 shows four arrows labeled segment 4, segment 5, segment 6, and segment 7 from the sender that points to the receiver. An arrow labeled ACK 8 from the receiver points to the sender.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig11.jpg)
    
    Figure 2-11: TCP Sliding Window
    
- **Buffering:** With buffering, a device (for example, a router) uses a chunk of memory (sometimes called a _buffer_ or a _queue_) to store segments if bandwidth is not available to send those segments. A queue has a finite capacity, however, and can overflow (that is, drop segments) in case of sustained network congestion.

In addition to TCP and UDP, Internet Control Message Protocol (ICMP) is another transport layer protocol you are likely to meet. ICMP is used by utilities such as ping and traceroute, which are discussed in Lesson 10, "Command-Line Tools."

### The Session Layer
The session layer, as shown in Figure 2-12, is responsible for setting up, maintaining, and tearing down sessions. You can think of a session as a conversation that needs to be treated separately from other sessions to avoid the intermingling of data from different conversations.  

![The figure depicts the key features of the session layer. The illustration shows the seven layers of the OSI model as a stack. The key features of the session layer are listed beside it that reads as follows: Setting up a session, Maintaining a session, and Tearing down a session.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig12.jpg)

Here is a detailed look at the functions of the session layer:

- **Setting up a session:** Examples of the procedures involved in setting up a session include the following:
    - Checking user credentials (for example, username and password)
    - Assigning numbers to a session's communication flows to uniquely find each one
    - Negotiating services needed during the session
    - Negotiating which device begins sending data
- **Maintaining a session:** Examples of the procedures involved in supporting a session include the following:
    - Transferring data
    - Reestablishing a disconnected session
    - Acknowledging receipt of data
- **Tearing down a session:** A session can be disconnected based on agreement of the devices in the session. Alternatively, a session might be torn down because one party disconnects (either intentionally or because of an error condition). If one party disconnects, the other party can detect a loss of communication with that party and tear down its side of the session.

H.323 is an example of a session layer protocol, which can help set up, support, and tear down a voice or video connection. Keep in mind, however, that not every network application neatly maps directly to all seven layers of the OSI model. The session layer is one of those layers where it might not be possible to name what protocol in each scenario is running in it. Network Basic Input/Output System (NetBIOS) is one example of a session layer protocol.



### The Presentation Layer
The presentation layer, as shown in Figure 2-13, handles formatting the data being exchanged and securing that data with encryption.  
  

![The figure depicts the key features of the presentation layer. The illustration shows the seven layers of the OSI model as a stack. The key features of the presentation layer are listed beside it that reads as follows: Data formatting and Encryption.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig13.jpg)

Figure 2-13: Layer 6-The Presentation Layer

  
The following list describes the function of data formatting and encryption in more detail:

- **Data formatting:** As an example of how the presentation layer handles data formatting, consider how text is formatted. Some applications might format text using American Standard Code for Information Interchange (ASCII), while other applications might format text using Extended Binary Coded Decimal Interchange Code (EBCDIC). The presentation layer handles formatting the text (or other types of data, such as multimedia or graphics files) in a format that allows compatibility between the communicating devices.
- **Encryption:** Imagine that you are sending sensitive information over a network (for example, your credit card number or bank password). If a malicious user were to intercept your transmission, they might be able to obtain this sensitive information. To add a layer of security for such transmissions, encryption can be used to scramble up (encrypt) the data in such a way that if the data were intercepted, a third party would not be able to unscramble it (decrypt). However, the intended recipient would be able to decrypt the transmission.

Encryption is discussed in detail in Lesson 12, "Network Security."  
  
### The Application Layer
The application layer, as shown in Figure 2-14, gives application services to a network. An important (and often-misunderstood) concept is that end-user applications (such as Microsoft Word) live at the application layer. Instead, the application layer supports services used by end-user applications. For example, email is an application layer service that does exist at the application layer, whereas Microsoft Outlook (an example of an email client) is an end-user application that does not live at the application layer. Another function of the application layer is advertising available services.  
  

![The figure depicts the key features of the application layer. The illustration shows the seven layers of the OSI model as a stack. The key features of the application layer are listed beside it that reads as follows: Application services and Service Advertisement.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig14.jpg)

Figure 2-14: Layer 7-The Application Layer

  
The following describes the functions of the application layer in more detail:

- **Application services:** Examples of the application services living at the application layer include file sharing and email.
- **Service advertisement:** Some applications' services (for example, some networked printers) periodically send out advertisements, making their availability known to other devices on the network. Other services, however, register themselves and their services with a centralized directory (for example, Microsoft Active Directory), which can be queried by other network devices seeking such services.

Recall that even though the application layer is numbered as Layer 7, it is at the top of the OSI stack because its networking functions are closest to the end user.

### Explanation

Here are the seven OSI layers and their functions:

1. **Physical****:** Transmits bits on the network with network characteristics
2. **Data link:** Packages data into frames and then transmits them on the network
3. **Network:** Forwards data on the basis of logical addresses
4. **Transport:** Encapsulates and decapsulates messages sent between upper and lower layers
5. **Presentation:** Formats the data being exchanged and secures that data by encryption
6. **Application:** Provides support for services used by an end-user

# 2.1.2 TCP/IP Stack
**Layers of the TCP/IP Stack**  
The TCP/IP stack has only four defined layers, as opposed to the seven layers of the OSI model. Figure 2-15 contrasts these two models for an illustrative understanding.  

![The figure shows the layers in the OSI and TCP/IP models which are displayed on the left and right, respectively. Layers in the OSI and TCP/IP models are displayed on the left and right, respectively. The layers in the OSI model from bottom to top are as follows: physical, data link, network, transport, session, presentation, and application. In the TCP/IP Model, the following layers are arranged similar to OSI model: Network interface (spanning across the last 2 boxes of OSI model), Internet (positioned parallel to the network layer of OSI Model), Transport (positioned parallel to the transport layer of OSI Model), and Application (spanning across the top 3 boxes of OSI Model).](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig15.jpg)
Figure 2-15: TCP/IP Stack
  
The TCP/IP stack is composed of the following layers:  

- **Network interface:** The TCP/IP stack's network interface layer encompasses the technologies offered by Layers 1 and 2 (the physical and data link layers) of the OSI model.  

    Note
    Some literature refers to the network interface layer as the _network access layer_.

- **Internet:** The Internet layer of the TCP/IP stack maps to Layer 3 (the network layer) of the OSI model. Although multiple routed protocols (for example, IP, IPX, and AppleTalk) live at the OSI model's network layer, the Internet layer of the TCP/IP stack focuses on IP as the protocol to be routed through a network. Figure 2-16 shows the format of an IP Version 4 packet.  
    ![The figure shows the format of an IP version 4 packet. The first layer is divided into two fields. The first field is partitioned into three sections: version, header length, and type of service. The second field is labeled total length. The second layer is divided into two fields. The first field is labeled identification. The second field is partitioned into two sections: IP flags and fragment offset. The third layer is divided into two fields. The first field is partitioned into two sections: TTL and protocol. The second field is labeled header checksum. The fourth layer has a single field that is labeled source address. The fifth layer has a single field that is labeled destination address. The sixth layer has a single field that is labeled IP option (variable length).](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig16.jpg)
    Figure 2-16: IP Version 4 Packet Format
      
    Notice that there are fields in the IP packet header for both a source and a destination IP address. The Protocol field shows the transport layer protocol from which the packet was sent or to which the packet should be sent. Also of note is the Time-to-Live (TTL) field. The value in this field is decremented by 1 every time this packet is routed from one IP network to another (that is, passes through a router). If the TTL value ever reaches 0, the packet is discarded from the network. This behavior helps prevent routing loops. As a common practice, the OSI layer numbers of 1, 2, and 3 are still used when referring to physical, data link, and network layers of the TCP/IP stack, even though the TCP/IP stack does not explicitly separate the physical and data link layers.
- **Transport:** The transport layer of the TCP/IP stack maps to Layer 4 (the transport layer) of the OSI model. The two primary protocols found at the TCP/IP stack's transport layer are TCP and UDP.  
      
    Figure 2-17 details the structure of a TCP segment. Notice the fields for source and destination ports. As described later in this lesson, these ports identify to which upper-layer protocol data should be forwarded, or from which upper-layer protocol the data is being sent.  
      
    
    ![The figure shows the structure of a TCP segments. The first layer is divided into two fields: source port and destination port. The second layer has a single field that is labeled sequence number. The third layer has a single field that is labeled acknowledgment number. The fourth layer is divided into two fields. The first field is divided into three sections: offset, reserved, and TCP flags. The second field is labeled window. The fifth layer is divided into two fields: checksum and urgent pointer. The sixth layer is labeled TCP options option (optional).](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig17.jpg)
    Figure 2-17: TCP Segment Format

    Also notice the field for window size. The value in this field determines how many bytes a device can receive before expecting an acknowledgment. As previously described, this feature offers flow control.  
      
    The header of a TCP segment also contains sequence numbers for segments. With sequence numbering, if segments arrive out of order, the recipient can put them back in the proper order based on these sequence numbers.  
      
    The acknowledgment number in the header shows the next sequence number the receiver expects to receive. This is a way for the receiver to let the sender know that all segments up to and including that point have been received. Due to the sequencing and acknowledgements, TCP is considered to be a _connection-oriented_ transport layer protocol.  
      
    Figure 2-18 presents the structure of a UDP segment. UDP is a connectionless, unreliable protocol. UDP lacks the sequence numbering, window size, and acknowledgment numbering present in the header of a TCP segment. The UDP segment's header simply contains source and destination port numbers, a UDP checksum (which is an optional field used to detect transmission errors), and the segment length (measured in bytes).  
      
    
    ![The figure shows the structure of UDP segments. The first layer is divided into two fields: source port and destination port. The second layer is divided into two fields: UDP length and UDP checksum.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig18.jpg)
    
    Figure 2-18: UDP Segment Format
    
      
    Because a UDP header is so much smaller than a TCP header, UDP becomes a good candidate for the transport layer protocol for applications that need to maximize bandwidth and do not require acknowledgments (for example, audio or video streams).
- **Application:** The biggest difference between the TCP/IP stack and the OSI model is found at the TCP/IP stack's application layer. This layer addresses concepts described by Layers 5, 6, and 7 (the session, presentation, and application layers) of the OSI model.

With the reduced complexity of a four-layer model like the TCP/IP stack, network designers and administrators can more easily categorize a given networking technology into a specific layer. For example, although H.323 was shown earlier as a session layer protocol within the OSI model, you would have to know more about the behavior of H.323 to properly categorize it. However, with the TCP/IP stack, you could quickly figure out that H.323 is a higher-level protocol that gets encapsulated inside of TCP, and thus classify H.323 in the application layer of the TCP/IP stack.  
  
**Common Application Protocols in the TCP/IP Stack**  
Application layer protocols in the TCP/IP stack are identifiable by unique port numbers. For example, when you enter a web address in an Internet browser, you are (by default) communicating with that remote web address using TCP port 80. Specifically, Hypertext Transfer Protocol (HTTP), which is the protocol used by web servers, uses TCP port 80. Therefore, the data you send to that remote web server has a destination port number of 80. That data is then encapsulated into a TCP segment at the transport layer. That segment is then further encapsulated into a packet at the Internet layer and sent out on the network using an underlying network interface layer technology such as Ethernet.  
  
Continuing with the example depicted in Figure 2-19, when you send traffic to that remote website, the packet you send out to the network needs not only the destination IP address (172.16.1.2 in this example) of the web server and the destination port number for HTTP (that is, 80), it also needs the source IP address of your computer (10.1.1.1 in this example). Because your computer is not acting as a web server, its port is not 80. Instead, your computer selects a source port number greater than 1023. In this example, let's imagine that the client PC selects the source port 1248.  
  

![The figure shows a client with IP Address 10.1.1.1 on the left and a web server with IP Address 172.16.1.2 on the right. A rightward arrow labeled as Source IP: 10.1.1.1, Source Port: 1248, Destination IP: 172.16.1.2, and Destination Port: 80 from the client points to the web server. A leftward arrow labeled as Source IP: 172.16.1.2, Source Port: 80, Destination IP: 10.1.1.1, and Destination Port: 148; from the web server points to the client.](https://s3.amazonaws.com/jigyaasa_content_static/Image2/02fig19.jpg)
Figure 2-19: Example: Port Numbers and IP Addresses

  
Notice that when the web server sends content back, the IP addresses and port numbers have now switched, with the web server as the source and your PC as the destination. With both source and destination port numbers, along with source and destination IP addresses, two-way communication becomes possible.

![[Pasted image 20230617235236.png]]
![[Pasted image 20230617235250.png]]
![[Pasted image 20230617235307.png]]

## CORRECT ANSWERS:
1. **Network interface:** This layer encompasses the technologies addressed by layers 1 and 2 (physical and data link layers) of the OSI model. The Network interface layer defines how data is physically sent through the network.
2. **Internet:** This layer maps to layer 3 (the network layer) of the OSI model. The Internet layer performs IP routing.
3. **Transport:** This layer maps to layer 4 (the transport layer) of the OSI model. The Transport layer manages communication sessions between host computers.
4. **Application:** This layer addresses the concepts described by layers 5, 6, and 7 (the session, presentation, and application layers) of the OSI model. The Application layer defines how host programs interface with the transport layer services to use the network.



# 2.2 Real World Case Study
Bob, a manager of the networking team at Acme, Inc., is paying extra attention to the specific words he uses as he talks to his team in preparation for the implementation of the network. When referring to transport protocols such as the connection-oriented TCP and the connectionless UDP, the word Bob uses to describe those protocol data units is _segment_.  
  
In discussing the applications that the company will be using over its network, Bob notes that many of these applications will be using TCP at the transport layer. This includes HTTP for web browsing, HTTPS for secure web traffic, and SMTP and IMAP for email services.  
  
The SSH protocol, which also uses TCP at the transport layer, is a secure method that the company will use to remotely connect to and manage its network devices. A common connectionless UDP protocol is DNS, which will be used thousands of times a day to translate a friendly name like [Pearson](http://www.pearson.com/) to an IP address that is reachable over the network. Another protocol based on UDP that will be used often is Dynamic Host Control Protocol (DHCP), which assigns client computers on the network an IP address that is required for sending and receiving Layer 3 packets.  
  
For the traffic on the LAN, the Ethernet cables and electronic signals being sent as bits going over those cables represent Layer 1 from an OSI perspective. On the LAN, they will be using Ethernet technology, and as a result the Layer 2 frames that are sent on the LAN will be encapsulated and sent as Ethernet Layer 2 frames.  
  
For datagrams being sent across the serial WAN connections provided by the service provider, it is likely that either PPP or HDLC encapsulation will be used for the Layer 2 frames. On both the LAN and the WAN, at Layer 3 (the network layer), IPv4 will be used for host addressing and defining networks. The same Layer 1, Layer 2, and Layer 3 infrastructure is also capable of transporting IPv6, if desired.  
  
Inside the Layer 3 IP headers, each packet contains the source and destination address, in addition to the information to tell the receiving network device about which Layer 4 transport protocol is encapsulated or carried inside of the Layer 3 packet. When a network device receives the packet and opens it up to look at the contents, this process is called _de-encapsulation_. As the recipient de-encapsulates and looks at the Layer 4 information, it identifies the application layer protocol or service being used. A segment going to a web server is likely to have a TCP destination port of 80 or 443, depending on whether encryption is being used for a secure connection. A DNS request uses a UDP destination port of 53.

# 2.3 Summary

Here are the main topics covered in this lesson:  

- The ISO's OSI reference model consists of seven layers: physical (Layer 1), data link (Layer 2), network (Layer 3), transport (Layer 4), session (Layer 5), presentation (Layer 6), and application (Layer 7). The purpose of each layer was presented, along with examples of technologies living at the individual layers, as it pertains to networking.
- The TCP/IP stack was presented as an alternative model to the OSI reference model. The TCP/IP stack consists of four layers: network interface, Internet, transport, and application. These layers were compared with the seven layers of the OSI model.
- This lesson discussed how port numbers are used to associate data at the transport layer with a proper application layer protocol. Examples of common application layer protocols in the TCP/IP suite were presented, along with their port numbers.


# Glossary

#### Open Systems Interconnection (OSI) reference model
Commonly referred to as the _OSI model_ or the _OSI stack_. This seven-layer model categorizes various network technologies.

#### protocol data unit (PDU)
The name given to data at different layers of the OSI model. Specifically, the PDU for Layer 4 is _segment_. The Layer 3 PDU is _packet_, the Layer 2 PDU is _frame_, and the Layer 1 PDU is _bit_.

#### current state modulation
One way to electrically or optically represent a binary 1 or 0 is to use current state modulation, which represents a binary 1 with the presence of voltage (on a copper cable) or the presence of light (on a fiber-optic cable). Similarly, the absence of light or voltage represents a binary 0.

#### state transition modulation
One way to electrically or optically represent a binary 1 or 0 is to use the transition between a voltage level (for example, going from a state of no voltage to a state of voltage, or vice versa, on a copper cable) or the transition of having light or no light on a fiber-optic cable to represent a binary 1. Similarly, a binary 0 is represented by having no transition in a voltage level or light level from one time period to the next. This approach of representing binary digits is called state transition modulation.

#### cyclic redundancy check (CRC)
A mathematical algorithm that is executed on a data string by both the sender and the receiver of the data string. If the calculated CRC values match, the receiver can conclude that the data string was not corrupted during transmission.

#### physical layer
Layer 1 of the OSI model. This layer is concerned with the transmission of bits on a network.

#### data link layer
As Layer 2 of the OSI model, this layer is concerned with the packaging of data into frames and transmitting those frames on a network, performing error detection/correction, uniquely identifying network devices with an address, and handling flow control.

#### network layer
Layer 3 of the OSI model. This layer is primarily concerned with forwarding data based on logical addresses.

#### transport layer (OSI model)
As Layer 4 of the OSI model, it acts as a dividing line between the upper layers and the lower layers. Specifically, messages are taken from the upper layers (Layers 5–7) and encapsulated into segments for transmission to the lower layers (Layers 1–3). Similarly, data streams coming from lower layers are decapsulated and sent to Layer 5 (the session layer) or some other upper layer, depending on the protocol.

#### session layer
As Layer 5 of the OSI model, it's responsible for setting up, maintaining, and tearing down sessions.

#### presentation layer
Layer 6 of the OSI model. This layer is responsible for the formatting of data being exchanged and securing the data with encryption.

#### application layer (OSI model)
Layer 7 of the OSI model. This layer provides application services to a network. An important yet often-misunderstood concept is that end-user applications do not reside at the application layer. Instead, the application layer supports services used by end-user applications. Another function of the application layer is advertising available services.

#### network interface layer
The network interface layer of the TCP/IP stack (also known as the _network access layer_) encompasses the technologies addressed by Layers 1 and 2 (that is, the physical and data link layers) of the OSI model.

#### Internet layer
This layer of the TCP/IP stack maps to Layer 3 (network layer) of the OSI model. Although multiple routed protocols (for example, IPv4 and IPv6) may reside at the OSI model's network layer, the Internet layer of the TCP/IP stack focuses on IP as the protocol to be routed through a network.

#### transport layer (TCP/IP stack)
The transport layer of the TCP/IP stack maps to Layer 4 (transport layer) of the OSI model. The two primary protocols found at the TCP/IP stack's transport layer are TCP and UDP.

#### application layer (TCP/IP stack)
Addresses concepts described by Layers 5, 6, and 7 (that is, the session, presentation, and application layers) of the OSI model.

#### time-division multiplexing (TDM)
Supports different communication sessions (for example, different telephone conversations in a telephony network) on the same physical medium by allowing sessions to take turns. For a brief period of time, defined as a time slot, data from the first session is sent, followed by data from the second session. This continues until all sessions have had a turn, and the process repeats itself.

#### Transmission Control Protocol (TCP)
A connection-oriented transport protocol. Connection-oriented transport protocols provide reliable transport, in that if a segment is dropped, the sender can detect that drop and retransmit that dropped segment. Specifically, a receiver acknowledges segments that it receives. Based on those acknowledgments, a sender can determine which segments were successfully received.

#### User Datagram Protocol (UDP)
A connectionless transport protocol. Connectionless transport protocols provide unreliable transport, in that if a segment is dropped, the sender is unaware of the drop, and no retransmission occurs.

#### TCP/IP stack
Also known as the _DoD model_, this four-layer model (as opposed to the seven-layer OSI model) targets the suite of TCP/IP protocols

