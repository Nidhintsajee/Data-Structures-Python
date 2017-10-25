class Node :
        def __init__( self, data ) :
                self.data = data
                self.next = None
                self.prev = None

        def get_data(self):
            return self.data

class LinkedList :
        def __init__( self ) :
                self.head = None		

        def add( self, data ) :
                node = Node( data )
                if self.head == None :	
                        self.head = node
                else :
                        node.next = self.head
                        node.next.prev = node						
                        self.head = node			

        def search( self, k ) :
                p = self.head
                if p != None :
                        while p.next != None :
                                if ( p.data == k ) :
                                        return p				
                                p = p.next
                        if ( p.data == k ) :
                                return p
                return None

        def remove( self, p ) :
                tmp = p.prev
                p.prev.next = p.next
                p.prev = tmp

        def size(self):
            current = self.head
            count=0
            while current:
                count+=1
                current=current.next
            return count
      
        def __str__( self ) :
                s = ""
                p = self.head
                if p != None :		
                        while p.next != None :
                                s += p.data
                                p = p.next
                        s += p.data
                return s
 
# example code
l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'c' )

print("List : "+str(l))
print("Deleted : b" )
l.remove( l.search( 'b' ) )
print("size : "+str(l.size()))
print("List : "+str(l)) 
