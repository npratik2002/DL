Parametric types refer to any type that can take a parameter. You can use parametric types in Verse to define generalized data structures and operations. There are two ways to use parametric types as arguments: either in functions as explicit or implicit type arguments, or in classes as explicit type arguments.

Events are a common example of parametric types and are used extensively throughout devices in UEFN. For instance, the Button device has the InteractedWithEvent, which occurs whenever a player interacts with the button. To see a parametric type in action, check out the CountdownEndedEvent from the Custom Countdown Timer Tutorial.

Explicit Type Arguments
Consider a box that takes two arguments. The first_item initializes an ItemOne, and the second_item initializes an ItemTwo, both of type type. Both first_item and second_item are examples of parametric types that are explicit arguments to a class.

box(first_item:type, second_item:type) := class:
    ItemOne:first_item
    ItemTwo:second_item
Because type is the type argument for first_item and second_item, the box class can be created with any two types. You could have a box of two string values, a box of two int values, a string and an int, or even a box of two boxes!

For another example, consider the MakeOption() function, which takes any type and returns an option of that type.

MakeOption(t:type):?t = false

IntOption := MakeOption(int)
FloatOption := MakeOption(float)
StringOption := MakeOption(string)
You could modify the MakeOption() function to instead return any other container type, such as an array or a map.

Implicit Type Arguments
Implicit type arguments for functions are introduced using the where keyword. For example, given a function ReturnItem(), which simply takes a parameter and returns it:

ReturnItem(Item:t where t:type):t = Item
Here, t is an implicit type parameter of the function ReturnItem(), which takes an argument of type type and immediately returns it. The type of t restricts what type of Item we can pass to this function. In this case since t is of type type, we can call ReturnItem() with any type. The reason to use implicit parametric types with functions is that it allows you to write code that works regardless of the type passed to it.

For example, instead of having to write:

ReturnInt(Item:int):int = Item

ReturnFloat(Item:float):float = Item
The single function could be written instead.

ReturnItem(Item:t where t:type):t = Item
This comes with the guarantee that ReturnItem() doesn't need to know what particular type the t is — whatever operation it performs, it will work regardless of the type of t.

The actual type to be used for t depends on how ReturnItem() is used. For example, if ReturnItem() is called with argument 0.0, then t is a float.

ReturnItem("t") # t is a string
ReturnItem(0.0) # t is a float
Here "hello" and 0.0 are the explicit arguments (the Item) passed to ReturnItem(). Both of these will work because the implicit type of Item is t, which can be any type.

For another example of a parametric type as an implicit argument to a function, consider the following MakeBox() function which operates on the box class.

box(first_item:type, second_item:type) := class:
    ItemOne:first_item
    ItemTwo:second_item

MakeBox(ItemOneVal:ValOne, SecondItemVal:ValTwo where ValOne:type, ValTwo:type):box(ValOne, ValTwo) =
    box(ValOne, ValTwo){ItemOne := ItemOneVal, ItemTwo := SecondItemVal}

Main():void =
    MakeBox("A", "B")
    MakeBox(1, "B")
    MakeBox("A", 2) 
    MakeBox(1, 2)
Here the MakeBox() function takes two arguments, FirstItemVal and SecondItemVal, both of type type, and returns a box of type (type, type). Using type here means we’re telling MakeBox that the returned box could be made up of any two objects; it could be an array, a string, a function, etc. The MakeBox() function passes both arguments to Box, uses them to create a box, and returns it. Note that both box and MakeBox() use the same syntax as a function call.

A built-in example of this is the function for the Map container type, given below.

Map(F(:t) : u, X : []t) : []u =
    for (Y : X):
        F(Y)
