# AddUsersToGroup.ps1
$OU = "OU=Users,OU=EGGTELSA,DC=eggtelsa,DC=net"
$Group = "CN=Grp-FileServer-Commun,OU=Grp-FileServer,OU=Groups,OU=EGGTELSA,DC=eggtelsa,DC=net"

# Get the distinguished name of the group
$GroupDN = (Get-ADGroup -Identity $Group).DistinguishedName

# Get all users in the specified OU
$Users = Get-ADUser -Filter * -SearchBase $OU

foreach ($User in $Users) {
    # Check if the user is already a member of the group
    $IsMember = Get-ADGroupMember -Identity $Group -Recursive | Where-Object { $_.DistinguishedName -eq $User.DistinguishedName }

    if (!$IsMember) {
        # Add the user to the group if they are not already a member
        Add-ADGroupMember -Identity $Group -Members $User
    }
}
